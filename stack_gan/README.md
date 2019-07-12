# StackGAN
### Text to Photo-Realistic Image Synthesis
---
#### Architecture
- Stage 1
	- Text Encoder Network
		- Text description to a 1024 dimensional text embedding
		- Learning Deep Representations of Fine-Grained Visual Descriptions [Arxiv](https://arxiv.org/abs/1605.05395)
	- Conditioning Augmentation Network
		- Adds randomness to the network
		- Produces more image-text pairs
	- Generator Network
	- Discriminator Network
	- Embedding Compressor Network
	- Outputs a 64x64 image
#
- Stage 2
	- Text Encoder Network
	- Conditioning Augmentation Network
	- Generator Network
	- Discriminator Network
	- Embedding Compressor Network
	- Outputs a 256x256 image
---
#### Checklist
- `tf.keras` with `tf.GradientTape()` training
- XLA Operations
- Distributed training (Mirrored Strategy)
- Evaluation and Tensorboard usage
- Pre-Trained Resnet
- CUB Dataset (11,788 images with 200 classes) with `TFRecords` and `tf.data.Dataset`
- Custom loss functions
- Export model ~ No Subclassing