# gestop

Built on top of [mediapipe](https://github.com/google/mediapipe), this project aims to be a tool to interact with a computer through hand gestures. Out of the box, using this tool, it is possible to:

1. Use your hand to act as a replacement for the mouse.
2. Perform hand gestures to control system parameters like screen brightness, volume etc.

In addition, it is possible to extend and customize the functionality of the application in numerous ways:

1. Remap existing hand gestures to different functions in order to better suit your needs.
2. Create custom functionality through the use of either python functions or shell scripts.
3. Collect data and create your own custom gestures to use with existing gestures. 

### [Demo video link](https://www.youtube.com/watch?v=K2UkIjK7BTI&t=19s)

#### [Models link](https://drive.google.com/drive/folders/16lbPkdYWcmLfx0oFo01A5FwTiCDK5DDK?usp=sharing)

#### [Dataset link](https://drive.google.com/drive/folders/1zMFQVKvpAhU-EKGxQNyFXKTu1TgBH23L?usp=sharing)

### Usage

In addition to the Python libraries in `requirements.txt`, [OpenCV](https://opencv.org/) and [xdotool](https://github.com/jordansissel/xdotool) are also required by Gestop.

#### Server

To start the **Gestop** server, do the following:

1. Clone this repo and install all its dependencies.
2. Execute the `get_models.sh` script to download the models and place the folder in the `gestop/` directory.
3. Start the server with the following command:

``` python
python gestop/gesture_receiver.py
```

*Note:* Python dependencies can be installed simply by creating a virtual environment and running `pip install -r requirements.txt`

#### Client

The client, or the *keypoint generator*, can be setup either through MediaPipe's C++ API, or through its Python API. The Python API is simpler to setup and is recommended.

#### MediaPipe Python API

Install the libraries required by `hand_tracking.py` i.e. **opencv** and **mediapipe**. Then, run the code with:

``` python
python gestop/keypoint_gen/hand_tracking.py
```

##### MediaPipe C++ API

1. Download mediapipe and set it up. MediaPipe >=0.8.0 is **NOT** supported and should no be used. Make sure the provided hand tracking example is working to verify if all dependencies are installed.
2. Clone this repo in the top level directory of mediapipe. Install all of Gestop's dependencies.
3. Run the instructions below to build and then execute the code. 

*Note:* Run build instructions in the `mediapipe/` directory, not inside this directory.

###### GPU (Linux only)
``` sh
bazel build -c opt --verbose_failures --copt -DMESA_EGL_NO_X11_HEADERS --copt -DEGL_NO_X11 gestop:hand_tracking_gpu

GLOG_logtostderr=1 bazel-bin/gestop/hand_tracking_gpu --calculator_graph_config_file=gestop/keypoint_gen/hand_tracking_desktop_live.pbtxt
```

###### CPU
``` sh
bazel build -c opt --define MEDIAPIPE_DISABLE_GPU=1 gestop:hand_tracking_cpu

GLOG_logtostderr=1 bazel-bin/gestop/hand_tracking_cpu --calculator_graph_config_file=gestop/keypoint_gen/hand_tracking_desktop_live.pbtxt
```

### Overview

The hand keypoints are detected using google's MediaPipe. These keypoints are then fed into `gesture_receiver.py` . The tool recognizes two kinds of gestures:

1. Static Gestures : Gestures whose meaning can be inferred from a single image itself.
2. Dynamic Gestures : Gestures which can only be understood through a sequence of images i.e. a video.

Static gestures, by default, are mapped to all functionality relevant to the mouse, such as left mouse click, scroll etc. Combined with mouse tracking, this allows one to replace the mouse entirely. The mouse is tracked simply by moving the hand, where the tip of the index finger reflects the position of the cursor. The gestures related to the mouse actions are detailed below. To train the neural network to recognize static gestures, a dataset was created manually for the available gestures.

For more complicated gestures involving the movement of the hand, dynamic gestures can be used. By default, it consists of various other actions to interface with the system, such as modifying screen brightness, switching workspaces, taking screenshots etc. The data for these dynamic gestures comes from [SHREC2017 dataset](http://www-rech.telecom-lille.fr/shrec2017-hand/). Dynamic gestures are detected by holding down the `Ctrl` key, which freezes the cursor, performing the gesture, and then releasing the key.

The project consists of a few distinct pieces which are:

* MediaPipe - Accessed through either the Python API or the C++ API, MediaPipe tracks the hand, generates the keypoints and transmits them.
* Gesture Receiver - See `gesture_receiver.py`, responsible for handling the stream and utilizing the following modules.
* Mouse Tracker - See `mouse_tracker.py`, responsible for moving the cursor using the position of the index finger.
* Gesture Recognizer - See `gesture_recognizer.py`, takes in the keypoints from the mediapipe executable, and converts them into a high level description of the state of the hand, i.e. a gesture name.
* Gesture Executor - See `gesture_executor.py`, uses the gesture name from the previous module, and executes an action.

### Notes

* For best performance, perform dynamic gestures with right hand only, as all data from SHREC is right hand only.
* For dynamic gestures to work properly, you may need to change the keycodes being used in `gesture_executor.py`. Use the given `find_keycode.py` script to find the keycodes of the keys used to change screen brightness and volumee. Finally, system shortcuts may need to be remapped so that the shortcuts work even with the Ctrl key held down. For example, in addition to the usual default behaviour of `<Prnt_Screen>` taking a screenshot, you may need to add `<Ctrl+Prnt_Screen>` as a shortcut as well. 

### [Customizing Gestop](CUSTOMIZATION.md)

### [Available Gestures](GESTURES.md)

<details>
<summary><b>Repo Overview</b></summary>
<br>
<ul>
<li> models -> Stores the trained model(s) which can be called by other files for inference </li>
<li> proto -> Holds the definitions of the protobufs used in the project for data transfer</li>
<li> BUILD -> Various build instructions for Bazel</li>
<li> <code>static_data_collection.py</code> -> Script to create a custom static gesture dataset.  </li>
<li> <code>dynamic_data_collection.py</code> -> Script to create a custom dynamic gesture dataset.  </li>
<li> <code>data/static_gestures_mapping.json</code> -> Stores the encoding of the static gestures as integers</li>
<li> <code>data/dynamic_gestures_mapping.json</code> -> Stores the encoding of the dynamic gestures as integers</li>
<li> <code>data/static_gestures_data.csv</code> -> Dataset created with data_collection.py </li>
<li> <code>data/action_config.json</code> -> Configuration of what gesture maps to what action. </li>
<li> <code>hand_tracking_desktop_live.pbtxt</code> -> Definition of the mediapipe calculators being used. Check out mediaipe for more details.</li>
<li> <code>hand_tracking_landmarks.cc</code> -> Source code for the mediapipe executable. GPU version is Linux only.</li>
<li> <code>model.py</code> -> Definition of the models used.</li>
<li> <code>static_train_model.py</code> -> Trains the "GestureNet" model for static gestures and saves to disk</li>
<li> <code>dynamic_train_model.py</code> -> Trains the "ShrecNet" model for dynamic gestures and saves to disk</li>
<li> <code>find_keycode.py</code> -> A sample program from pynput used to find the keycode of the key that was pressed. Useful in case the brightness and audio keys vary.</li>
<li> <code>gesture_receiver.py</code> -> Handles the stream of data coming from the mediapipe executable by passing it to the various other modules.</li>
<li> <code>mouse_tracker.py</code> -> Functions which implement mouse tracking.</li>
<li> <code>gesture_recognizer.py</code> -> Functions which use the trained neural networks to recognize gestures from keypoints.</li>
<li> <code>gesture_executor.py</code> -> Functions which implement the end action with an input gesture. E.g. Left Click, Reduce Screen Brightness</li>
<li> <code>config.py</code> -> Stores the configuration and state of the application in dataclasses for easy access. </li>
<li> <code>user_config.py</code> -> Stores the definition of all the actions that will be executed when a particular gesture is detected. </li>
</ul>
</details>

### Useful Information

[Joints of the hand](https://en.wikipedia.org/wiki/Interphalangeal_joints_of_the_hand)

[HandCommander](https://www.deuxexsilicon.com/handcommander/)

[Video recorded with VokoScreenNG](https://github.com/vkohaupt/vokoscreenNG)
