# README                                                                       
                                                                               
Motion Photo splitter for Google Camera
                                                               
**Requirements** 

- Linux / OSX 
- Python 2.7.x     

## Converting pictures                                                               
                                                                      
### Linux  / OSX

- Place the script in the directory where the images are
- Open the terminal  
  **OSX**: ⌘(Command) + Space, type “Terminal” and then hit “Enter”

  **Linux** : Ctrl + Alt + t
- Run the script  
                                                                                                                                
 ```bash                                                                        
 for p in *.jpg; do                                                            
    python splitter.py ${p}                                                     
  done                                                                          
 ``` 
