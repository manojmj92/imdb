#~/.gnome2/nautilus-scripts
IFS_BAK=$IFS
IFS="
"

     full_path="/home/"$USER"/Desktop/"imdb-folder.py
     folder= $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
        
        python $full_path $folder


IFS=$IFS_BAK
