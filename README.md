# Professional Cover Letter and Resume Generator

This application employs the Flask web framework to provide a streamlined web service. Upon visiting the home page, users can input the title of the position they are applying for and submit the form to initiate the creation of a tailored cover letter. The job title is processed through the OpenAI API to generate a unique cover letter, which is subsequently stored in a Word document named `cover_letter.docx` at the root directory of the project.

The application is currently hosted at [cover-letter-assist.fly.dev](https://cover-letter-assist.fly.dev/) by the reputable hosting service [fly.io](https://fly.io/). The intuitive interface, easy-to-navigate documentation, and overall user experience offered by fly.io are exceptional. Although I have no professional affiliation with the company, I can confidently endorse fly.io for your project hosting needs based on my personal experience.

## Application Walkthrough:

1. **Launch the Application:** Use the command `flask run` in your terminal to start the application.
   ![flask run](https://user-images.githubusercontent.com/99860222/215569860-65f5ecfc-9688-411c-ab68-e445521fcb7f.png)

2. **Access the Application:** Click on the http://127.0.0.1:5000/ link to access the home page of the application.
   ![localhost](https://user-images.githubusercontent.com/99860222/215570017-04685a75-c1f1-49ab-b152-aaa9fcc0f512.png)

3. **Home Page:** Here's what the home page looks like.
   ![HomePage](https://user-images.githubusercontent.com/99860222/223607491-065c2d2f-0346-4167-9264-bb00b9bf4633.png)

4. **Generate Cover Letter:** Enter the title of the position you are applying for in the provided input box, and click on 'Create Cover Letter' to initiate the process.
   ![position](https://user-images.githubusercontent.com/99860222/223607549-71fd7d42-d4a7-479d-98a5-001877b6f65a.png)

5. **View and Use the Cover Letter:** Scroll down to view the generated cover letter. You can directly copy and paste the content into your preferred text editor and customize it according to your requirements.

6. **Finished Cover Letter:** The final cover letter will be displayed in the text box upon scrolling down.

   ![CoverLetter](https://user-images.githubusercontent.com/99860222/223607969-183aa11c-d67c-4e3a-8970-ea8ce921f413.png)

7. **Mission Accomplished:**

![mic drop](https://user-images.githubusercontent.com/99860222/215571932-dc36a660-2f3d-4c31-884a-d6aa5c54b9c2.png)
