
### What I need…

A pictures gallery in a directory usualy contains a great numer of files wich names look random, even if the names follow the same pattern…

In my situation, I had a gallery with 293 JPEG pictures. the name pattern was:
- the string `IMG_`,
- a 4 digits number, with one (or more) leading zeros if necessary: _ie._ 0243,
- the `.jpeg` suffix.

My first file name was `IMG_0211.jpeg` and the last one `IMG_1505.jpeg`.  
I want the files to be renamed from `IMG_0001.jpeg` to `IMG_0293.jpeg`…  
And I'm not going to rename 293 files by hand!

### What to do…

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



