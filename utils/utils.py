import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid
import os
import torch
from PIL import Image


def sample_image(model, encoder, output_image_dir, n_row, batches_done, dataloader, device):
    """Saves a grid of generated imagenet pictures with captions"""
    target_dir = os.path.join(output_image_dir, "samples/")
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)

    captions = []
    gen_imgs = []
    # get sample captions
    done = False
    while not done:
        for (_, labels_batch, captions_batch) in dataloader:
            captions += captions_batch
            conditional_embeddings = encoder(labels_batch.to(device), captions)
            imgs = model.sample(conditional_embeddings).cpu()
            gen_imgs.append(imgs)

            if len(captions) > n_row ** 2:
                done = True
                break

    gen_imgs = torch.cat(gen_imgs).numpy()
    gen_imgs = np.clip(gen_imgs, 0, 1)

    fig = plt.figure(figsize=((8, 8)))
    grid = ImageGrid(fig, 111, nrows_ncols=(n_row, n_row), axes_pad=0.2)

    for i in range(n_row ** 2):
        grid[i].imshow(gen_imgs[i].transpose([1, 2, 0]))
        grid[i].set_title(captions[i])
        grid[i].tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=True)

    save_file = os.path.join(target_dir, "{:013d}.png".format(batches_done))
    plt.savefig(save_file)
    print("saved  {}".format(save_file))
    plt.close()


def sample_image2(model, encoder, output_image_dir, n_row, n_col, batches_done, dataloader, device):
    """Saves a grid of generated imagenet pictures with captions"""
    print('sample_image2', n_row, n_col)
    target_dir = os.path.join(output_image_dir, "samples/")
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)

    captions = []
    gen_imgs = []
    # get sample captions
    done = False
    while not done:
        i = 0
        for (_, labels_batch, captions_batch) in dataloader:
            print('ITERATION', i)
            captions += captions_batch[0:n_row*n_col]
            conditional_embeddings = encoder(labels_batch[0:n_row*n_col].to(device), captions)
            imgs = model.sample(conditional_embeddings).cpu()
            gen_imgs.append(imgs)

            if len(captions) >= n_row * n_col:
                done = True
                break
            i += 1

    gen_imgs = torch.cat(gen_imgs).numpy()
    gen_imgs = np.clip(gen_imgs, 0, 1)

    fig = plt.figure(figsize=((8, 8)))
    grid = ImageGrid(fig, 111, nrows_ncols=(n_row, n_col), axes_pad=0.2)

    for i in range(n_row * n_col):
        grid[i].imshow(gen_imgs[i].transpose([1, 2, 0]))
        grid[i].set_title(captions[i])
        grid[i].tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=True)

        single_image_path = os.path.join(target_dir, "{:013d}_{:03d}.png".format(batches_done, i))
        print('single_image_path', single_image_path)
        plt.imsave(single_image_path, gen_imgs[i].transpose([1, 2, 0]))

    save_file = os.path.join(target_dir, "{:013d}.png".format(batches_done))
    plt.savefig(save_file)
    print("saved  {}".format(save_file))
    plt.close()


def load_model(file_path, generative_model):
    dict = torch.load(file_path)
    generative_model.load_state_dict(dict)