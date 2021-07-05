import inscription
from train_model import trainModel
import face_rec

def main():
    ques=''
    ques=input("you want to add new faces?[Y/n] ")
    if ques.lower() == 'y':
        fname = input("Saisir le prenom: ")
        lname = input("Saisir le nom: ")
        age = input("Saisir l'age: ")
        print("Now We'll take a pics of you...")
        inscription.shot(fname)
#    ans = input("Is the database created?[Y/n] ")
#    if ans.lower() == 'n':
#        inscription.create_db()
        inscription.con(fname,lname,age)

        print("Training the Model...")
        trainModel()
        print("face recognition....")
        
    face_rec.faceRec()

    
  

if __name__ == "__main__":
    main()
