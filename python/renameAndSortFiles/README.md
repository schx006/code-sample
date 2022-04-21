
# What I need…

A pictures gallery in a directory usualy contains a great numer of files wich names look random, even if the names follow the same pattern…

In my situation, I had a gallery with 293 JPEG pictures. the name pattern was:
- the string `IMG_`,
- a 4 digits number, with one (or more) leading zeros if necessary: _ie._ 0243,
- the `.jpeg` suffix.

My first file name was `IMG_0211.jpeg` and the last one `IMG_1505.jpeg`.  
I want the files to be renamed from `IMG_0001.jpeg` to `IMG_0293.jpeg`…  
And I'm not going to rename 293 files by hand!

This Python script will do the job for me.

# How to…

1. The script needs the two subdirectories `filesToSort` and `sortedFiles` in the same directory as itself (the _working directory_).
2. Copy (or move) the picture files into the `filesToSort` subdirectory.  
   The `sortedFiles` subdirectory must be empty.  
   ![Directory screenshot](https://github.com/schx006/code-sample/blob/main/pictures/filesToSort_screenshot.png)
3. Open a `Terminal.app` window:
   - go into the _working directory_,
   - run the command:  
     ```sh  
     python3 ./renameAndSortFiles
     ```  
   The `filesToSort` subdirectory should now be empty.
4. Move the renamed and sorted files to their new gallery folder.

# Warning!

The script…

# Customise it.

This script is easily customisable. The format of the sorted file names is contained in 3 variables:

```Python

fName = "IMG_"
fSuffix = ".jpeg"
i = 1

```
For example:

1. If you prefer to name the sorted files `pict-xxxx.jpeg` instead of `IMG_xxxx.jpeg`, change the `fName` variable as follows:
   ```Python
   fName = "pict-"
   ```
2. If you prefer to use the 3-letter suffix (`IMG_xxxx.jpg`), change the `fSuffix` variable as follows:
   ```Python
   fSuffix = ".jpg"
   ```
3. If your images are not in JPEG format, but in PNG format, change the `fSuffix` variable as follows:
   ```Python
   fSuffix = ".png"
   ```
4. To enlarge a gallery, you will have to continue counting from the existing file number (Nₘₐₓ).
   You need to initialize the counter `i` with the number Nₘₐₓ + 1.  
   As my gallery already contains 293 pictures, the first file name of the series to be added should be `IMG_0294.jpeg`:
   ```Python
   i = 294
   ```
5. You can also sort sound files in the same way...
   ```Python
   fName = "SOUND_"
   fSuffix = ".mp3"
   i = 1
   ```

And so on.
