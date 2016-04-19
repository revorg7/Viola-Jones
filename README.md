# Viola-Jones 0.1
Viola-Jones framework in Python

This software uses a single Adaboost classifier for now. I plan to implement the cascade-classifier soon. It depends upon the following libraries: scikit-learn,scikit-image, numpy, scipy, PIL. It also uses Joblib library for test/detection part for now.

This is a masters project implementation, currently in the beta-phase, but my experience suggests that the training is not as slow as suggested by others using the opencv implementation. I exchange time for memory. So atleast 8gigs of RAM is must for training phase.

Here is what I did:
final.py: I assumed a 19X19 dataset(http://cbcl.mit.edu/software-datasets/FaceData2.html). Calculated harr-like features on it, saved as numpy-array. It took ~20 mins for 2500 samples on my i5,8gigs system.

"NO SCRIPT PROVIDED FOR THIS PART": Used scikit-learn to train my model on this numpy-array(~20 mins) for training-data of 471 positive and 5000 negative samples. The trained-model is pickled as bdt.pkl.

IN THE TEST FLODER:
sliding_window.py: Took an image, heurestically choose window-size, downsampled each window to 19X19, calculated (all)harr-features, and created new numpy-array. Then tested the model on these windows and plotted the detected windows.

#TODO
In detection phase, not all harr-features needs to be calculated(that was the whole-idea of Viola-Jones framework). But since I cannot directly extract the underlying decision-stumps used in my sklearn-adaboost model. I have to bear with it for now. Thus it takes ~15 mins even to detect in a single image for now.
