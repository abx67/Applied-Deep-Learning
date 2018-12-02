def generate_images(slide_path,zoom_level,x=0,y=0,
                    window_size=2,stride=1):
  """This function will generate images from slide
  
  Arguments:
    slide_path: path of slide
    zoom_level: the level that we want to look at
    x,y: start coordinates
    window_size: size of the window used to get images from slide
    stride: step
      
  Returns:
    returns sub-images array from slide
    
  """
  
  slide = open_slide(slide_path)
  width, height = slide.level_dimensions[zoom_level]
  img=read_slide(slide, x=x, y=y, level=zoom_level, width, height, as_float=False)
  num_pad=window_size-stride
  pad_img=np.pad(img, (num_pad,num_pad), 'constant', constant_values=0)
  pad_img=pad_img[:,:,1:4]
  
  imgs=[]
  for i in range(pad_img.shape[0],stride):
    for j in range(pad_img.shape[1],stride):
      grid=pad_img[i:(i+window_size),j:(j+window_size)]
      imgs.append(grid)
  
  return imgs  