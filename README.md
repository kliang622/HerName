# 🌹 Rose Hack 2022 - *Her Name* (Won 3rd Place)

> Devpost: 
https://devpost.com/software/her-story

 > Authors: [Audrey Kim](https://github.com/Audrey-Kim), [Kanin Liang](https://github.com/kliang622), [Nathan Melwani](https://github.com/NateM135), and [Paulian Le](https://github.com/paulian7)

# Inspiration
- When we think of trailblazers in tech, we often go back to the same group of male Silicon Valley CEOs. Unfortunately, pioneers such as Ada Lovelace, the first computer programmer, and Reshma Saujani, the founder of Girls Who Code, rarely come to mind. Through *Her Name*, our team wanted to reform this and bring lesser-known leaders, specifically those who identify as women, into the spotlight through three core steps: empowerment, connection, and educate.

# What it does
- *Her Name* aims to raise awareness about various accomplished women through a fun but simple mechanic. When a user uploads a photo to our website, our software will return a female innovator they most resemble from our database.
- We ultimately hope to give well-deserved recognition to the figures we show our users as well as educate our users, especially those who identify as female, on role models in fields that are traditionally filled with men.

# How we built it
- Our project consists of a user interface, so the user can engage with our software, and a server, where our facial-recognition magic happens behind the scenes.
- We utilized HTML and CSS to create an intuitive interface that displays information about our project, directs user engagement, and communicates with our application's backend.
- For the backend, we created an API with Python using Flask. This API uses Google's Cloud Vision Facial Detection API to determine where in an uploaded photo a face is located by giving us the coordinates of the face in an image. Next, OpenCV is used to extract said face and compare it against those in our database. The figure with the highest percentage match to the user's face is then displayed to the user.

# Challenges we ran into
- Some challenges we ran into included attempting to match our users' faces to those in our project as accurately as possible. Towards the beginning of the hackathon, the algorithm we used to match images wasn't polished, resulting in inaccuracies between the test photos we provided and those in our gallery.

# Accomplishments that we're proud of
- In accordance with the challenge we mentioned above, we were able to match certain uploaded faces with those that we determined had the most similar characteristics in our directory. We're also proud of our UI -- we worked really hard on it over the past day!

# What we learned
- One of the concepts we learned was constructing a HTTP API for uploading image files. A more prominent idea we also learned was implementing Jinja, a server side template language that let us define variables in HTML pages. We also learned how to set up proper authentication and authorization in order to safely use Google Cloud's APIs.

# What's next for *Her Name*
- We recognize that there are additional opportunities for further development on Her Name. One operation we can execute is expanding our index of role models. This can allow for a more diverse variety of users to successfully learn about someone they truly identify with.
- We also are aware of a security vulnerability on our program. Since there is no human verification or rate limiting present on our site, users are able to upload as many images as their internet speed allows. Each picture submission makes a call to the Cloud Vision API, which costs a certain amount of money to access. This can quickly result in a sizable Google Cloud bill for our team.
