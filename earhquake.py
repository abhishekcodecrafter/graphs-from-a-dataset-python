from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

# Sample earthquake data
earthquake_data = [
    {"Date": "2023-07-21", "Time": "04:09 AM", "Magnitude": 4.4,
        "Depth": "10 km", "Epicenter": "Jaipur district, Rajasthan, India"},
    {"Date": "2023-07-21", "Time": "04:11 AM", "Magnitude": 3.1,
        "Depth": "10 km", "Epicenter": "Jaipur district, Rajasthan, India"},
    {"Date": "2023-07-21", "Time": "04:13 AM", "Magnitude": 2.9,
        "Depth": "10 km", "Epicenter": "Jaipur district, Rajasthan, India"},
    {"Date": "2023-07-21", "Time": "04:15 AM", "Magnitude": 2.5,
        "Depth": "10 km", "Epicenter": "Jaipur district, Rajasthan, India"},
]

# Locations affected by the earthquake in Jaipur
jaipur_locations = [
    "Mansarover",
    "Bani Park",
    "Jawahar Nagar",
    "Sanganer",
    "Jhotwara",
    "Bapu Nagar",
    "Ramgarh",
    "Jagatpura",
    "Gopalpura",
]

# Locations affected by the earthquake in surrounding areas
surrounding_locations = [
    "Sikar",
    "Dausa",
    "Alwar",
    "Jhunjhunu",
    "Bharatpur",
]

# Additional locations near Jaipur
near_jaipur_locations = [
    "Kanakpura",
    "Shyam Nagar",
    "Vaishali Nagar",
    "Tonk Road",
]

# Create a DataFrame from the earthquake data
df = pd.DataFrame(earthquake_data)


@app.route('/')
def index():
    jaipur_len = len(jaipur_locations)
    surrounding_len = len(surrounding_locations)
    near_jaipur_len = len(near_jaipur_locations)

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Earthquake Graphs</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.16/dist/tailwind.min.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <script src="https://kit.fontawesome.com/e674bba739.js" crossorigin="anonymous"></script>
        <style>
        body {
            background-color: black;
        }
        .card {
            background-color: #222;
            color: silver;
        }
        .card-header {
            background-color: #333;
            color: silver;
        }
        h1, h3, h4, h5 {
            color: white !important;
        }
        /* Adjust table data color */
        table {
            color: silver;
            border-collapse: collapse;
            width: 100%;
        }
        th {
            color: white;
            background-color: #444;
            padding: 8px;
            text-align: left;
        }
        td {
            color : white;
            background-color: #333;
            padding: 8px;
            border-bottom: 1px solid #444;
        }

        /* ---------- SECTION HEADER ---------- */
        #header {
          padding: 20px 40px;
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: #2d2e3273;
          border: 1px solid #2d2e3240;
          box-shadow: 0 0 10px 1px #00000040;
          backdrop-filter: blur(15px);
          color: #fefefe;
          z-index: 1;
          top: 0;
          left: 0;
          margin: 0;
        }               
                                          
                .navbar-title {
          display: flex;
          align-items: center;
        }
        
        .title-first-name {
          padding: 0 7.5px;
          font-weight: 600;
          color: #fefefe;
          font-family: "Raleway", sans-serif;
          font-size: 24px;
        }
        
        .title-last-name {
          font-size: 24px;
          font-weight: 400;
          color: #cacaca;
          font-family: "Raleway", sans-serif;
        }
        
        .navbar-menu {
          display: flex;
          justify-content: center;
          align-items: center;
        }
        
        .navbar-menu li {
          list-style: none;
          padding: 0 20px;
          position: relative;
        }
        
        .navbar-menu .active {
          color: #64f4ac;
          font-weight: 900;
        }
        
        .navbar-menu li a {
          color: #fefefe;
          text-decoration: none;
          font-size: 12px;
          font-weight: 600;
          transition: 0.3s ease;
        }
        
        .navbar-menu li a:hover {
          color: #64f4ac;
          font-weight: 900;
        }
        
        .social-media {
          display: flex;
          align-items: center;
          right:0;
        }
        
        .social-media li {
          display: flex;
          padding: 0 16px;
          align-items: center;
          list-style: none;
        }
        
        .social-media li i {
          font-size: 14px;
          transition: 0.3s ease;
        }
        .social-media li a {
          color: #fefefe;
          text-decoration: none;
          padding: 0 5px;
          font-size: 12px;
          transition: 0.3s ease;
        }
        
        .social-media li:nth-child(1):hover i {
          color: #0077b5;
        }
        
        .social-media li:nth-child(3):hover i {
          color: #ea4335;
        }
        
        .social-media li:hover a {
          font-weight: 800;
        }
                                  
        @import url("https://fonts.googleapis.com/css2?family=Raleway:wght@100;200;300;400;500;600;700;800;900&family=Source+Code+Pro:wght@200;300;400;500;600;700;800;900&display=swap");
        /* ---------- GLOBAL STYLING ---------- */
        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
          font-family: "Raleway", sans-serif;
          font-family: "Source Code Pro", monospace;
        }
        
        html {
          scroll-behavior: smooth;
        }
        
        h1 {
          font-size: 50px;
          font-weight: 400;
          line-height: 64px;
          color: #fefefe;
        }
        
        h2 {
          font-size: 46px;
          line-height: 54px;
          font-weight: 400;
          color: #fefefe;
        }
        
        h4 {
          font-size: 20px;
          font-weight: 400;
          color: #fefefe;
        }
        
        h6 {
          font-weight: 700;
          font-size: 12px;
          color: #fefefe;
        }
        
        p {
          font-size: 16px;
          font-weight: 400;
          color: #fefefe;
          margin: 15px 0 20px 0;
        }
        
        .section-p1 {
          padding: 40px 80px;
        }
        
        .section-m1 {
          margin: 40px 0;
        }
        
        button.normal {
          font-size: 14px;
          font-weight: 600;
          padding: 15px 30px;
          color: black;
          background-color: white;
          border-radius: 4px;
          cursor: pointer;
          border: none;
          outline: none;
          transition: 0.5s ease;
        }
        
        button.normal:hover {
          font-size: 14px;
          font-weight: 600;
          padding: 15px 30px;
          color: #fff;
          background-color: #088178;
        }
        
        body {
          width: 100%;
          background-color: #2d2e32;
        }
        
        body::selection {
          color: #000000;
          background: #64f4ac;
        }
        
        ::-webkit-scrollbar{
          width: 10px;
        }
        
        ::-webkit-scrollbar-track{
          background: transparent;
        }
        
        ::-webkit-scrollbar-thumb{
          background: #CACACA;
          transition: 0.3s ease;
          border-radius: 15px;
        }
        
        ::-webkit-scrollbar-thumb:hover{
          background: #FEFEFE;
        }

        /* ----------FOOTER---------- */
#footer {
  display: flex;
  flex-direction: row;
  padding: 80px; /* Decreased padding for better appearance in the example, adjust as needed */
  background-color: #25262a;
  height: 10vh;
  bottom: 0;
  margin-top: 60px;
}

.footer-right {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  flex-grow: 1;
}

.footer-right h6,
.footer-right p,
.footer-right h3 {
  color: white;
  margin: 5px 0;
}

.social-icons {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-end;
  flex-grow: 1;
}

.social-icons a {
  text-decoration: none;
  margin: 0 5px;
}

.social-icons a i {
  color: #fff;
  transition: 0.3s ease;
  cursor: pointer;
}

.social-icons a:nth-child(1) i:hover {
  color: #0072b1;
}

.social-icons a:nth-child(3) i:hover {
  color: #ea4335;
}

.social-icons a:nth-child(4) i:hover {
  color: #00acee;
}

.social-icons a:nth-child(5) i:hover {
  color: transparent;
  background: -webkit-radial-gradient(30% 107%, circle, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
  background: -o-radial-gradient(30% 107%, circle, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
  background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
  background: -webkit-radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
  background-clip: text;
  -webkit-background-clip: text;
}

.social-icons a:nth-child(6) i:hover {
  color: #3b5998;
}
        
                                  
        /* Add any additional styles as needed */
    </style>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
       <section id="header">
        <div class="navbar-title">
            <h3 class="title-first-name">
                Abhishek
            </h3>
            <h3 class="title-last-name">
                Mahala
            </h3>
        </div>
        <div>
            <ul class="social-media">
                <li>
                    <i class="fa-brands fa-instagram"></i>
                    <a href="https://instagram.com/abhishek._.developer" target="_blank">Instagram</a>
                </li>
                <li>
                    <i class="fa-brands fa-github"></i>
                    <a href="https://github.com/abhishekcodecrafter" target="_blank">Github</a>
                </li>
                <li>
                    <i class="fa-regular fa-envelope"></i>
                    <a href="mailto:abhishekm01012004@gmail.com">Email</a>
                </li>
            </ul>
        </div>
    </section>



        <div class="container mt-5">
            <h1 class="text-4xl font-bold mb-5" style="color:white;">Jaipur's Earthquake Information</h1>
            <div class="card">
                <div class="card-header">
                    <h3 class="font-bold text-lg">Earthquake Magnitude (Bar Chart)</h3>
                </div>
                <div class="card-body">
                    <canvas id="magnitudeChart" style="max-height: 400px;"></canvas>
                </div>
            </div>

            <div class="card mt-5">
                <div class="card-header">
                    <h3 class="font-bold text-lg">Earthquake Depth (Line Chart)</h3>
                </div>
                <div class="card-body">
                    <canvas id="depthChart" style="max-height: 400px;"></canvas>
                </div>
            </div>

            <div class="card mt-5">
                <div class="card-header">
                    <h3 class="font-bold text-lg">Earthquake Distribution (Pie Chart)</h3>
                </div>
                <div class="card-body">
                    <canvas id="distributionChart" style="max-height: 700px;"></canvas>
                </div>
            </div>

            <!-- Display the names of areas -->
            <div class="card mt-5">
                <div class="card-header">
                    <h3 class="font-bold text-lg">Affected Areas</h3>
                </div>
                <div class="card-body">
                    <ul>
                        <li>Jaipur (जयपुर)</li>
                        {% for loc, color in area_data %}
                        <li>{{ loc }} ({{ loc }})</li>
                        {% endfor %}
                        <li>Near Jaipur ({{ near_jaipur_locations|join(', ') }})</li>
                        <li>Surrounding Areas</li>
                        {% for loc in surrounding_locations %}
                        <li>{{ loc }} ({{ loc }})</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>

            <div class="card mt-5">
                <div class="card-header">
                    <h3 class="font-bold text-lg">Earthquake Impact Information</h3>
                </div>
                <div class="card-body">
                    <p>
                        Here, is a Table about the earthquake in Jaipur:
                    </p>
                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Time</th>
                                <th>Magnitude</th>
                                <th>Depth</th>
                                <th>Epicenter</th>
                                <th>Impact</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for _, row in df.iterrows() %}
                            <tr>
                                <td>{{ row['Date'] }}</td>
                                <td>{{ row['Time'] }}</td>
                                <td>{{ row['Magnitude'] }}</td>
                                <td>{{ row['Depth'] }}</td>
                                <td>{{ row['Epicenter'] }}</td>
                                <td>No major damage or injuries reported. Some people shaken up by tremors.</td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                    <p>
                        The earthquake occurred in the Jaipur district of Rajasthan, India. The epicenter of the earthquake was located 10 km from Jaipur. The earthquake lasted for about 20 seconds. There were no reports of major damage or injuries due to the earthquake. However, some people were shaken up by the tremors.
                    </p>
                    <p>
                        The earthquake was felt in several other parts of Rajasthan, as well as in neighboring states like Haryana, Punjab, and Uttar Pradesh. It was also felt in some parts of Delhi and Uttarakhand.
                    </p>
                    <p>
                        The National Disaster Management Authority (NDMA) has advised people to stay calm and follow safety guidelines in case of an earthquake. These guidelines include staying away from buildings and other structures that could collapse, and taking shelter under a sturdy table or desk if you are indoors.
                    </p>
                </div>
            </div>
        </div>
                                
        <!-- Footer -->
        <section id="footer">
        <div class="footer-right">
            <div class="footer-email-intro">
                <p>Address Information</p>
                <h6>Sikar,Straight Jaipur Highway,In Front of NAvjeevan RBSE School,Sikar,Rajasthan,India,Pin-332001</h6>
                <h3>abhishekm01012004@gmail.com</h3>
            </div>
            <div class="social-icons">
                <a href="https://www.linkedin.com/in/abhishek-mahala-a62784283" target="_blank">
                    <i class="fa-brands fa-linkedin-in"></i>
                </a>
                <a href="https://github.com/abhishekcodecrafter" target="_blank">
                    <i class="fa-brands fa-github"></i>
                </a>
                <a href="mailto:abhishek01012004@gmail.com" target="_blank">
                    <i class="fa-regular fa-envelope"></i>
                </a>
                <a href="https://twitter.com/Abhishe5082675" target="_blank">
                    <i class="fa-brands fa-twitter"></i>
                </a>
                <a href="https://www.linkedin.com/in/abhishek._.developer/" target="_blank">
                    <i class="fa-brands fa-instagram"></i>
                </a>
                <a href="https://www.facebook.com/abhishek.mahala.58/" target="_blank">
                    <i class="fa-brands fa-facebook"></i>
                </a>
            </div>
        </div>
    </section>

        <script>
            // Chart.js code to create the charts
            var magnitudeCtx = document.getElementById('magnitudeChart').getContext('2d');
            var depthCtx = document.getElementById('depthChart').getContext('2d');
            var distributionCtx = document.getElementById('distributionChart').getContext('2d');

            // Data for the charts
            var magnitudeData = {
                labels: [{% for _, row in df.iterrows() %}"{{ row['Time'] }}", {% endfor %}],
                datasets: [{
                    label: 'Magnitude',
                    data: [{% for _, row in df.iterrows() %}{{ row['Magnitude'] }}, {% endfor %}],
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }],
            };

            var depthData = {
                labels: [{% for _, row in df.iterrows() %}"{{ row['Time'] }}", {% endfor %}],
                datasets: [{
                    label: 'Depth (in km)',
                    data: [{% for _, row in df.iterrows() %}{{ row['Depth'].split()[0] }}, {% endfor %}],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }],
            };

            var distributionData = {
                labels: ['Jaipur (जयपुर)', {% for loc in jaipur_locations %}'{{ loc }} ({{ loc }})', {% endfor %}
                         'Near Jaipur ({{ near_jaipur_locations|join(", ") }})',
                         'Surrounding Areas', {% for loc in surrounding_locations %}'{{ loc }} ({{ loc }})', {% endfor %}],
                datasets: [{
                    data: [1, {% for _ in jaipur_locations %}1, {% endfor %}
                           {{ near_jaipur_len }},
                           1, {% for _ in surrounding_locations %}1, {% endfor %}],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 192, 203, 0.2)',
                        'rgba(255, 0, 0, 0.2)',
                        'rgba(0, 0, 255, 0.2)',
                        'rgba(128, 0, 128, 0.2)',
                        'rgba(139, 69, 19, 0.2)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(255, 192, 203, 1)',
                        'rgba(255, 0, 0, 1)',
                        'rgba(0, 0, 255, 1)',
                        'rgba(128, 0, 128, 1)',
                        'rgba(139, 69, 19, 1)',
                    ],
                    borderWidth: 1
                }],
            };

            // Chart options
            var options = {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            };

            // Create the charts
            new Chart(magnitudeCtx, {
                type: 'bar',
                data: magnitudeData,
                options: options
            });

            new Chart(depthCtx, {
                type: 'line',
                data: depthData,
                options: options
            });

            new Chart(distributionCtx, {
                type: 'pie',
                data: distributionData,
                options: options
            });
        </script>
                                  
        <script>
  // Get the header element
  const header = document.getElementById("header");
  let prevScrollPos = window.pageYOffset;

  // Function to toggle the header visibility
  function toggleHeaderVisibility() {
    const currentScrollPos = window.pageYOffset;

    if (prevScrollPos > currentScrollPos) {
      // Scrolling up
      header.classList.remove("header-hidden");
    } else {
      // Scrolling down
      header.classList.add("header-hidden");
    }

    prevScrollPos = currentScrollPos;
  }

  // Attach the scroll event listener
  window.addEventListener("scroll", toggleHeaderVisibility);
</script>
    </body>
    </html>
    ''', df=df, jaipur_len=jaipur_len, near_jaipur_len=near_jaipur_len, surrounding_len=surrounding_len, jaipur_locations=jaipur_locations, near_jaipur_locations=near_jaipur_locations, surrounding_locations=surrounding_locations)


if __name__ == '__main__':
    app.run(debug=True)
