import tkinter
import random
import tkinter.messagebox
import requests
import time



# Simple joke generation app that utilises open api from which the jokes are retrieved
def main():

    def reenable_button():
        generate_joke_btn.config(state="normal")

    # puts a "GET" request to the api url and returns data in dictionary
    def generate_joke():
        api_url = "https://official-joke-api.appspot.com/random_joke"
        headers = {
            "content-type" : "application/json",
            "accept" : "application/json",
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
        
        try:
            response = requests.get(api_url,headers=headers)
            if response.status_code == 200:
                joke_dict = response.json()
                return joke_dict
            else:
                 raise Exception(f"API returned status code: {response.status_code}")
        except Exception as e:
             tkinter.messagebox.showerror("Error",f"Something went wrong. Check Your Internet Connection. \nError Message: {e}")
            
    # Function that handles the joke generation and displaying of joke to the gui
    def start_joke_generator():
        
        try:
                joke_dict = generate_joke()
                

                joke_type.config(state="normal"), joke_type.delete(0,tkinter.END), joke_type.insert(0,joke_dict["type"]), joke_type.config(state="disabled") # Inserting the type of joke to entry


                joke_setup.config(state="normal"), joke_setup.delete("1.0",tkinter.END), joke_setup.insert(tkinter.END,joke_dict["setup"]), joke_setup.config(state="disabled") # Inserting the joke body to text box

                joke_punchline.config(state="normal"), joke_punchline.delete("1.0",tkinter.END), joke_punchline.insert(tkinter.END,joke_dict["punchline"]), joke_punchline.config(state="disabled") # Inseting the joke punchline to text box

                generate_joke_btn.config(state="disabled"), joke_app.after(int(random.uniform(3000,5500)),reenable_button)#time.sleep(random.uniform(3, 5.5)), generate_joke_btn.config(state="normal") # Throtting to show politness
        except Exception as e:
            tkinter.messagebox.showerror("Error",f"Something Went wrong. Error message: {e}")

    # The GUI implementation
    joke_app = tkinter.Tk()
    joke_app.title("Random Jokes Generator")
    joke_app.geometry("400x300")


    joke_type_label = tkinter.Label(joke_app, text="JOKE TYPE: ")
    joke_type_label.grid(row=0, column=0)
    joke_type = tkinter.Entry(joke_app, text="",state="disabled")
    joke_type.grid(row=0, column=1,)

    blank_1 = tkinter.Label(joke_app)
    blank_1.grid(row=1)

    joke_setup_label = tkinter.Label(joke_app,text="THE JOKE: ")
    joke_setup_label.grid(row=2, column=0)
    joke_setup = tkinter.Text(joke_app,width=38,height=5,state="disabled")
    joke_setup.grid(row=2, column=1,)

    blank_2 = tkinter.Label(joke_app)
    blank_2.grid(row=3)

    joke_punchline_label = tkinter.Label(joke_app,text="PUNCHLINE: ")
    joke_punchline_label.grid(row=4, column=0)
    joke_punchline = tkinter.Text(joke_app,width=38, height=5,state="disabled")
    joke_punchline.grid(row=4, column=1)


    blank_3 = tkinter.Label()
    blank_3.grid(row=5)

    generate_joke_btn = tkinter.Button(joke_app,width=10,text="Generate",command=start_joke_generator)
    generate_joke_btn.grid(row=6, column=0)

    

    joke_app.mainloop()

if __name__ == "__main__":
    main()