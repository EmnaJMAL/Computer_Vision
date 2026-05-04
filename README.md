# Computer Vision Mini-Project — Augmented Reality with Human Skeleton Extraction

This project implements several computer vision and augmented reality features using a 2D/3D human skeleton extracted from video. It was developed for the Computer Vision course and is based on OpenCV and the `lightweight-human-pose-estimation-3d-demo.pytorch` model.

## Project Goals

The project is divided into two parts:

1. **Pre-recorded video interaction**  
   Notebook: `Human-object-interaction-from-video-partial.ipynb`

2. **Live webcam interaction**  
   Notebook: `Human-pose-interaction-live-partial.ipynb`

The implemented features are:

- face blurring to preserve anonymity;
- background blurring;
- background replacement with an artificial image;
- insertion of a 3D cube/house object attached to the user’s left hand;
- recording the processed output into playable video files.

## Project Structure

```text
.
├── Human-object-interaction-from-video-partial.ipynb
├── Human-pose-interaction-live-partial.ipynb
├── Mini-projet-final.pdf
└── data/
    ├── video-with-human.mp4
    ├── human-skeleton-poses.bin
    ├── office-background.png
    ├── your-mini-project-output.mp4
    └── live-output.mp4
```

> Note: the files inside `data/` must be available for the notebooks to run correctly.

## Requirements

The project requires:

- Python 3;
- Jupyter Notebook;
- OpenCV;
- NumPy;
- Matplotlib;
- the `lightweight-human-pose-estimation-3d-demo.pytorch` repository/model;
- a webcam for the live part.

Before opening the notebooks, run the following commands in a Linux terminal:

```bash
SETUP HRI
export PYTHONPATH=/opt/campux/lightweight-human-pose-estimation-3d-demo.pytorch/:
```

## Installing Python Dependencies

If needed, install the main Python libraries with:

```bash
pip install opencv-python numpy matplotlib jupyter
```

Depending on the practical lab environment, some dependencies related to the human pose estimation model may already be installed.

## How It Works

### 1. Pre-computed Skeleton from Video

In `Human-object-interaction-from-video-partial.ipynb`, the program reads:

- an input video: `data/video-with-human.mp4`;
- a pre-computed 2D pose file: `data/human-skeleton-poses.bin`;
- a background image: `data/office-background.png`.

For each frame, the human skeleton is loaded and used to apply the visual effects.

### 2. Live Skeleton Detection

In `Human-pose-interaction-live-partial.ipynb`, the human pose is estimated directly from the webcam stream using the model:

```text
/opt/campux/lightweight-human-pose-estimation-3d-demo.pytorch/human-pose-estimation-3d.pth
```

The video stream is processed frame by frame and saved as `data/live-output.mp4`.

## Implemented Features

### Face Blurring

The face is blurred using the skeleton joint corresponding to the head. A square region around this joint is extracted, and an OpenCV `GaussianBlur` filter is applied to that region.

Example principle:

```python
blurred_img = cv2.GaussianBlur(mask, (25, 25), 10)
final_frame[y1:y2, x1:x2] = blurred_img
```

### Background Blurring

A mask is created from the human skeleton. The skeleton mask is then dilated to cover a wider area around the body. The full image is blurred, and the non-blurred person area is copied back from the original frame.

Main steps:

1. create an empty mask;
2. draw the skeleton on the mask;
3. dilate the mask using `cv2.dilate`;
4. blur the full frame;
5. merge the sharp person region with the blurred background.

### Background Replacement

Background replacement uses the same masking principle as background blurring:

- a person mask is generated from the skeleton;
- the background image is resized to match the video frame size;
- the person is kept from the original frame;
- the rest of the frame is replaced with `office-background.png`.

### 3D Object Attached to the Left Hand

A simple 3D cube/house object is defined using:

- a list of 3D vertices;
- a list of edges connecting the vertices.

The object is projected into the 2D image around the left-hand skeleton joint and drawn with `cv2.line`. In the live version, a rotation is applied to the object based on the frame index.

## Keyboard Controls

During notebook execution, the following keys enable or disable the effects:

| Key | Action |
|---|---|
| `f` | Toggle face blurring |
| `b` | Toggle background blurring |
| `s` | Toggle background replacement |
| `o` | Toggle the 3D object attached to the hand |
| `d` | Show/hide the skeleton, only in the live version |
| `p` | Pause/resume the video |
| `Space` | Continue after pausing |
| `Esc` | Quit the application |

## Running the Project

### Part 1 — Pre-recorded Video

Open the notebook:

```bash
jupyter notebook Human-object-interaction-from-video-partial.ipynb
```

Then run the cells in order.

The output video is saved as:

```text
data/your-mini-project-output.mp4
```

### Part 2 — Live Webcam Stream

Open the notebook:

```bash
jupyter notebook Human-pose-interaction-live-partial.ipynb
```

Then run the cells in order.

The output video is saved as:

```text
data/live-output.mp4
```

## Important Parameters

### Pre-recorded Video Notebook

```python
parser.add_argument('--video', default='data/video-with-human.mp4')
parser.add_argument('--bg_image', default='data/office-background.png')
```

### Live Notebook

```python
parser.add_argument('--video', default='0')
parser.add_argument('--model', default='/opt/campux/lightweight-human-pose-estimation-3d-demo.pytorch/human-pose-estimation-3d.pth')
parser.add_argument('--device', default='GPU')
parser.add_argument('--height-size', default=256)
```

## Generated Outputs

| File | Description |
|---|---|
| `data/your-mini-project-output.mp4` | Processed result for the pre-recorded video |
| `data/live-output.mp4` | Processed result for the live webcam stream |

## Limitations and Possible Improvements

- The body mask is based on the skeleton, so some body regions may not be fully covered.
- Face blurring depends on the accuracy of the detected head joint.
- Background replacement could be improved with semantic segmentation.
- The 3D object uses a simplified camera projection.
- Object stability depends on the quality of the left-hand detection.

Possible improvements:

- use a segmentation model to isolate the person more precisely;
- smooth skeleton coordinates to reduce jitter;
- add multiple interactive 3D objects;
- improve depth and collision handling;
- add a user interface to select effects in real time.

## Author

Mini-project completed as part of the Computer Vision course — Augmented Reality via Human Skeleton Extraction.
