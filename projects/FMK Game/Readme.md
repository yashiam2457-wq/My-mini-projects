========================================================
                Welcome To SP/FMK
========================================================
Project Tree
Folder
  |-----Dataprep
  |      |----datacollect.py
  |
  |-----main.py
  |-----Anime.mmap
  |-----Superhero.mmap
  |-----Game.mmap
  |-----category.txt
========================================================
DataBases
    |--Anime.mmap
    |--Superhero.mmap
    |--Game.mmap
Database Format- [Category, Character, image bytes]
========================================================
Libraries Used
    |---PyQt6
    |---mmap
    |---os
    |---random
    |---struct
========================================================
Caution during Data preparation-                        
* Make sure category list- [Category, subcategory, No of
characters] and Data upload on mmap- [Category, 
Character, image path] must be correct
* category list- [subcategory] and mmap- [category] must
be exact same, even with string space for searching for
data in mmap 
========================================================