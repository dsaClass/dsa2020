inorder=list(input())
postorder=list(input())
def main(ino,poso,pre,k):
    if k==1:
        print(pre+'*')
    elif ino:
        ro=poso[-1]
        print(pre+ro)
        lef_ino,rig_ino=ino[:ino.index(ro)],ino[ino.index(ro)+1:]
        k=0
        if rig_ino and not lef_ino :
            k=1
        main(lef_ino,poso[:len(lef_ino)],pre+'\t',k)
        main(rig_ino,poso[len(lef_ino):-1],pre+'\t',0)
main(inorder,postorder,'',0)