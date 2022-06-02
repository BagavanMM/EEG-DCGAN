# Using Deep-Convolutional GANs to Improve SSVEP Classification Systems
**Implemented a DCGAN based-on the paper: [Simulating Brain Signals: Creating Synthetic EEG Data via Neural-Based Generative Models for Improved SSVEP Classification](https://arxiv.org/pdf/1901.07429.pdf)**


<!-- ABOUT THE PROJECT -->
## About this Project
In this project, I created a Deep-Convolutional Generative Adversarial Network (DCGAN) that generates synthetic EEG data for SSVEP classification. 

**In order to capture these brain signals, we use something known as a brain-computer interface.** 
Whenever you’re doing anything, from talking, playing video games, to even reading this article, billions of neurons in our brain are constantly firing. **A brain-computer interface is that’s used to capture these brain signals, analyze them and translate them into a specific output or command.** Now, a lot of methods used for capturing our brain signals using BCIs are generally invasive/semi-invasive, meaning you’d have to undergo some kind of surgery to implant electrodes into your brain. However, that isn’t going to be practical for this project, and scaling any project/product. That’s why one of the most common ways of collecting this data is through a non-invasive method known as electroencephalography (EEG).

Electroencephalography (or EEG for short) is what’s used to collect electrical activity from the brain, by placing electrodes (small metal discs with thin wires) onto the scalp/surface of your head. These electrodes are what are used to detect different changes in electrical charge due to activity from your brain waves.

<br>**The Problem:** EEG classification systems tend ot have a low accuracy, and the root cause stems from the lack of high-quality data; collecting high-quality EEG data in large quantities has been very difficult for various reasons like the high reliance on careful per-subject calibration, fewer bad channels, etc.

That’s when I came across the idea of using creating synthetic EEG data to improve classification systems.

I decided to implement a Deep-Convolutional GAN from the paper mentioend above.

***For more information about DCGANs and the problem, feel free to check out this [article](https://bagavanmm.medium.com/using-deep-convolutional-gans-to-increase-ssvep-classification-systems-15794c5f8189)***



Here's an overview of the files:
 - `data_preprocess.py` is a file that preprocesses the EEG data <br>
 - `DCGAN.ipynb` is the notebook that contains our DCGAN <br>
 - `Gen.py` is the file that generates the synthetic data <br>
 - `Data/` contains sample data for our model <br>

## Dependencies and Requirements
The project was built in Python V3.7 (can run in python 3.6+ only), and requires the following libraries:
 - [torch=1.1.0+](https://pytorch.org/docs/stable/torch.html)
 - [numpy=1.16+](https://numpy.org/)
 - [scipy=1.1.0+](https://scipy.org/)

<!-- CONTACT -->
## Contact

Bagavan Marakathalingasivam - [@BagavanMM](https://twitter.com/BagavanMM) - bagavan.sivam@gmail.com

Project Link: [https://github.com/BagavanMM/EEG-DCGAN](https://github.com/BagavanMM/EEG-DCGAN)

