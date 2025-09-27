import os
ext=".png"
l=os.listdir("clutter/")
for j in range(len(l)):
    if (l[j]).endswith('.png'):
        p=l[j]
        z=f"{j+1}{ext}"
        if(p!=z):
            if z not in l:
                os.rename(f"clutter/{p}",f"clutter/{z}")