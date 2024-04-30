import imageio.v3 as iio

filenames = ['jhin1_resize.png', 'jhin2_resize.png']
images = []

for filename in filenames:
	images.append(iio.imread(filename))

iio.imwrite('jhin.gif', images, duration = 500, loop = 0)
