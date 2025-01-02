hangman-game (Python project) 

عمل الطالبتان : سدرة بشار عماد الدين السقال , غفران مرعي ابراهيم درغام


تم استخدام dataset مكونة من

19 rows and 10 columns

تتكون البيانات من عدة مجموعات (category) وكل مجموعة تحتوي 10 كلمات


شرح الكود :

استخدمنا مكتبة numpy  للتعامل مع الملفات dataset 

واستخدمنا مكتبة matplotlip للرسم البياني (عدد مرات اختيار الحرف الصحيحة والخاطئة)

استخدمنا مكتبة random  لاختيار الكلمات بشكل عشوائي داخل الfile بدونها سيتم اختيار نفس الكلمة 

انشأنا class اسمه hangman 

وعرفنا function init  ليستقبل
2 parameters = oldfile and newfile

تم انشاء dic خاص بالcategory حتى تتوزع الكلمات ل key:value

استخدم for loop من اجل قراءة واستخراج كل key , value من الملف المرفق

self.category = np.random.choice(list(self.categories.keys()))

اختيار category بشكل عشوائي 

self.word = np.random.choice(self.categories[self.category])

اختيار word بشكل عشوائي بناءً على ال category الذي تم اختياره سابقا

self.guessed_letters = []

عملنا متغير = tuple فارغة لوضع الاحرف التي يتم تخمينها فيه 

self.remaining_tries = 6

self.correct_guesses = 0

self.incorrect_guesses = 0

عدد الاخطاء المسموح فيها 

عدد التخمينات الصحيحة 

عدد التخمينات الغير صحيحة


ثم تم عمل function خاص من أجل اللاعب اذا كان يرغب بإكمال اللعبة او لا يقوم هذا الfun بإعادة ضبط :

1)اختيار category and word  بشكل عشوائي مرة اخرى

2)عدد الاخطاء المسموح بها الى 6

3)والاحرف التي سيتم تخمينها الى tuple فارغة

def display_word(self):

     display = ''
     
       for letter in self.word:
       
           if letter in self.guessed_letters:
           
               display += letter
               
           else:
           
               display += '_'
               
        return display
يقوم هاد الfun باستبدال الاحرف الغير مخمنة من الكلمة المختارة ب ( _ ) وعندما يتم تخمين حرف موجود بالكلمة سيقوم بإظهاره لللاعب


(ملاحظة : هناك fun اخر خاص بالتخمين الاحرف اذا كان صحيح او لا)


   def make_guess(self, letter):
   
        if self.remaining_tries > 0: عدد المحاولات اقل من 0
        
            if letter.isalpha() and len(letter) == 1: يتأكد ان الحرف المدخل هو حرف وليس رقم او رمز
            
                letter = letter.lower()يقوم بتحويل الحرف الى حرف صغير 
                
                if letter not in self.guessed_letters:
                
                    self.guessed_letters.append(letter)
                    
                    يضيف الحرف المخمن الى guessed letters إن لم يكن فيها 
                    
                    if letter not in self.word:
                    
                        self.remaining_tries -= 1
                        
                        self.incorrect_guesses += 1
                        
                        اذا كان الحرف غير موجود في الكلمة المختارة يتم تقليل عدد المحاولات الخاطئة المسموحة بواحد وزيادة قيمة التخمينات الخاطئة بواحد
                        
                    else:
                    
                        self.correct_guesses += 1
                        
                        يقوم بزيادة واحد للتخمينات الصحيحة اذا لم يتحقق الشرط في الاعلى
                        
                    return True
                    
        return False
        

  def check_win(self):
  
        for letter in self.word:
        
            if letter not in self.guessed_letters:
            
                return False
                
        return True
        
يستخدم هذا الfun لمعرفة اذا كان اللاعب قد فاز في اللعبة ام لا 

عن طريق أنه يفحص الحرف الحالي بالكلمة(التي تم اختيارها بشكل عشوائي) هل هو غير موجود بالاحرف التي تم تخمينها بمعنى ان اللاعب لم يخمن احرف الكلمة كاملة فيعيد false لكن لو ان الحرف موجود من ضمن الاحرف التي تم تخمينها فيعيد true
بمعنى ان اللاعب قد نجح بتخمين كل الاحرف 


   def add_category(self, category, words):
   
        if category in self.categories:
        
            self.categories[category].extend(words)
            
        else:
        
            self.categories[category] = words
            
            الهدف من هذا الfun  هو إضاف category جديدة الشرط بيفحص اذا الفئة الي بدي اضيفها موجودة بس بضيف الكلمات 
            
            اذا مش موجودة بضيفها (key) مع الكلمات 
            

  def save_to_new_file(self):
  
        with open(self.new_filename, "w") as new_file:
        
            for category, words in self.categories.items():
            
                new_file.write(f"{category}\t{', '.join(words)}\n")
                
                في هذا الfun بحكيله يفتح الملف الجديد على اساس الكتابة ("w") ويقوم بتخزين البيانات القديمة + اخر فئة انا ضفتها لملف جديد اسمه new file
                



def play(self):

        while True:لوب من اجل استمرار اللعبة 
        
            self.reset_game()بدأ لعبة جديدة
            
            while self.remaining_tries > 0 and not self.check_win():
            
            شرط اللوب الثاني ان يكون عدد المحاولات اكبر من 0 واللاعب لم يخمن كل الاحرف بشكل صحيح
            
                print(f"\nCategory: {self.category}")طباعة الفئة المختارة 
                
                print(f"Word: {self.display_word()}")طباعة الكلمة بشكل مخفي في البداية 
                
                print("Used letters:", ', '.join(self.guessed_letters))طباعة الاحرف
                
                print("Remaining tries:", self.remaining_tries)طباعة عدد المحاولات
                
                guess = input("Enter a letter: ").strip()يطلب من اليوزر ادخال حرف
                
                              strip()  يقوم بإزالة أي مسافات زائدة من بداية ونهاية النص المدخل
                              
              .
                if self.make_guess(guess):يفحص الاجابة اذا كانت fulse or true
                
                    if self.check_win():
                    
                        print(f"\nCongratulations! You won! The word was: {self.word}")
                        
                        break اذا true  بيطبع هي الجملة 
                        
                else:
                
                    print("Please enter a valid unused letter")
                    
                    اذا اعطانيfulse يعني انه دخل حرفين او اكثر او انه دخل رمز او رقم فبيطبع هي الجملة 
                    
            if self.remaining_tries == 0:
            
                print(f"\nGame Over! The word was: {self.word}")اذا خلص عدد المحاولات بيطبعها
                
            
            
            play_again = input("Do you want to play again? (yes/no): ").strip().lower() 
            
            يسأل اللاعب اذا بده يكمل لعب او لا واذا كتب اي شئ غير YES  بيطبعله الجملة الي بالاسفل
            self.plot_results()  احصائية

            
            if play_again != 'yes':
            
                print("Thanks for playing Hangman! Goodbye!")
                
                break 
                

هاد الfun خاص بمكتبة الmat تهدف إلى عرض إحصائيات التخمينات (الصحيحة والخاطئة) التي قام بها اللاعب باستخدام رسم بياني

       def plot_results(self):
       
        categories = ['Correct Guesses', 'Incorrect Guesses'] قائمة تحتوي على أسماء الفئات التي تمثل أنواع التخمينات
        
        values = [self.correct_guesses, self.incorrect_guesses] قائمة تخص عدد التخمينات الصحيحة
        
        plt.bar(categories, values, color=['green', 'red'])  x=categorys   y=values  and color
        
        plt.xlabel('Guess Type')تسمية الافقي 
        
        plt.ylabel('Number of Guesses')تسمية العامودي
        
        plt.title('Hangman Guess Statistics')تسمية الرسم البياني
        
        plt.show() لعرض الرسم البياني
        


استدعينا الكلاس وبعثناله ملف ال old and new 

وبعثنا الcategory الجديدة وحفظناها بnewfile 


filename_old = "oldfile.txt"

filename_new = "newfile.txt"

game = Hangman(filename_old, filename_new)

game.add_category("Fruits", ["apple", "banana", "orange", "grape", "pear", "cherry", "fig", "kiwi", "watermelon", "blueberry"])

game.save_to_new_file()

game.play() 




                
