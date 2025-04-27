import os
import base64
import streamlit as st


def get_base64_of_bin_file(bin_file):
  with open(bin_file, 'rb') as f:
    data = f.read()
  return base64.b64encode(data).decode()


def support_icon(
        path_contact_button,
        path_first_social,
        path_second_social,
        path_mail,
        target_url_mail
):
  img_format_button = os.path.splitext(path_contact_button)[-1].replace('.', '')
  bin_str_button = get_base64_of_bin_file(path_contact_button)

  img_format_telegram = os.path.splitext(path_first_social)[-1].replace('.', '')
  bin_str_telegram = get_base64_of_bin_file(path_first_social)

  img_format_whatsapp = os.path.splitext(path_second_social)[-1].replace('.', '')
  bin_str_whatsapp = get_base64_of_bin_file(path_second_social)

  img_format_mail = os.path.splitext(path_mail)[-1].replace('.', '')
  bin_str_mail = get_base64_of_bin_file(path_mail)

  # CSS styling
  def load_css():
      # Main CSS
      st.markdown("""
      <style>
      /* Main theme colors */
      :root {
          --primary: #2d78c9;
          --primary-light: #64a1e0;
          --primaryButton: #629677;
          --dark: #1a222c;
          --light: #f8f9fa;
          --gray: #6c757d;
          --success: #28a745;
      }

        .st-emotion-cache-1104ytp a {
            color: grey;
            text-decoration-style: solid;
            text-decoration-color: currentcolor;
            text-decoration: none;
        }

      /* Typography */
      h1, h2, h3, h4, h5, h6 {
          font-family: 'Poppins', sans-serif;
          font-weight: 600;
      }

      p, li, a {
          font-family: 'Inter', sans-serif;
          font-size: 1rem;
          line-height: 1.6;
      }

      /* Page structure */
      .main-container {
          max-width: 1200px;
          margin: 0 auto;
          padding: 0 1rem;
      }

      /* Header styling */
      .header {
          text-align: center;
          padding: 2rem 0;
      }

      .header h1 {
          font-size: 2.5rem;
          margin-bottom: 0;
          color: var(--dark);
      }

      .header h5 {
          font-size: 1.25rem;
          color: var(--gray);
          font-weight: 400;
      }

      /* Profile image */
      .profile-image {
          border-radius: 50%;
          border: 5px solid white;
          box-shadow: 0 4px 10px rgba(0,0,0,0.1);
          transition: transform 0.3s ease;
      }

      .profile-image:hover {
          transform: scale(1.05);
      }

      /* Social icons */
      .social-icons {
          display: flex;
          justify-content: center;
          margin: 1.5rem 0;
      }

      .social-icon {
          width: 40px;
          height: 40px;
          margin: 0 10px;
          transition: transform 0.2s ease;
      }

      .social-icon:hover {
          transform: scale(1.15);
      }

      /* Section styling */
      .section {
          margin: 2.5rem 0;
          padding: 1.5rem 0;
          border-top: 1px solid #eee;
      }

      .section-title {
          font-size: 1.75rem;
          color: var(--primary);
          margin-bottom: 1.5rem;
          display: flex;
          align-items: center;
      }

      .section-title:after {
          content: "";
          flex-grow: 1;
          height: 1px;
          background: #eee;
          margin-left: 1rem;
      }

      /* Cards */
      .card {
          background: white;
          border-radius: 10px;
          box-shadow: 0 4px 10px rgba(0,0,0,0.105);
          padding: 1.5rem;
          margin-bottom: 1.5rem;
          transition: transform 0.3s ease, box-shadow 0.3s ease;
      }

      .card-skill {
          background: white;
          border-radius: 10px;
          box-shadow: 0 4px 10px rgba(0,0,0,0.105);
          padding: 1.5rem;
          margin-bottom: 1.5rem;
          #transition: transform 0.3s ease, box-shadow 0.3s ease;
      }

      # .card:hover {
      #     transform: translateY(-5px);
      #     box-shadow: 0 8px 15px rgba(0,0,0,0.1);
      # }

      /* Timeline for experience */
      .timeline-item {
          position: relative;
          padding-left: 25px;
          margin-bottom: 1.5rem;
          border-left: 2px solid var(--primary-light);
      }

      .timeline-date {
          font-weight: 600;
          color: var(--primary);
          margin-bottom: 0.5rem;
      }

      .timeline-role {
          font-weight: 600;
          font-size: 1.1rem;
          margin-bottom: 0.5rem;
      }

      .timeline-company {
          font-style: italic;
          color: var(--gray);
          margin-bottom: 1rem;
      }

      /* Skills formatting */
      .skill-category {
          font-weight: 600;
          color: var(--dark);
          margin-bottom: 0.5rem;
      }

      .skill-tag {
          display: inline-block;
          background: lightgrey;
          color: #629677;
          padding: 0.25rem 0.75rem;
          border-radius: 20px;
          font-size: 0.9rem;
          margin: 0.25rem;
      }

      /* Project cards */
      .project-card {
          display: flex;
          flex-direction: column;
          height: 100%;
      }

      .project-image {
          border-radius: 10px;
          margin-bottom: 1rem;
          object-fit: cover;
          max-height: 290px;
      }

      .project-title {
          font-size: 1.25rem;
          font-weight: 600;
          margin-bottom: 0.75rem;
      }

      .project-description {
          flex-grow: 1;
          margin-bottom: 1rem;
      }

      .project-tech {
          margin-bottom: 1rem;
      }

      .project-link {
          display: inline-block;
          background: white;
          color: grey;
          padding: 0.5rem 1rem;
          border-radius: 5px;
          text-decoration: none;
          transition: background 0.3s ease;
          border: 1px solid lightgrey;
      }

      .project-link:hover {
          background: white;
          color: var(--primaryButton);
          border: 1px solid var(--primaryButton);
      }


      .project-link:active {
          background: var(--primaryButton);
          color: white;
          border: 1px solid var(--primaryButton);
      }

      /* Stats cards */
      .stat-card {
          text-align: center;
          padding: 1.5rem;
      }

      .stat-number {
          font-size: 2.5rem;
          font-weight: 700;
          color: var(--primary);
          margin-bottom: 0.5rem;
      }

      .stat-label {
          color: var(--gray);
      }

      /* Contact section */
      .contact-item {
          display: flex;
          align-items: center;
          margin-bottom: 1rem;
      }

      .contact-icon {
          width: 24px;
          margin-right: 10px;
      }

      /* Floating contact button */
      .float-contact {
          position: fixed;
          right: 30px;
          bottom: 30px;
          background-color: var(--primary);
          color: white;
          width: 60px;
          height: 60px;
          border-radius: 50%;
          text-align: center;
          box-shadow: 0 4px 10px rgba(0,0,0,0.2);
          display: flex;
          align-items: center;
          justify-content: center;
          cursor: pointer;
          z-index: 999;
          transition: background 0.3s ease;
      }

      .float-contact:hover {
          background-color: var(--dark);
      }

      /* Responsive */
      @media (max-width: 768px) {
          .header h1 {
              font-size: 2rem;
          }

          .section-title {
              font-size: 1.5rem;
          }

          .project-image {
              height: 150px;
          }
      }

      /* Remove Streamlit default styling */
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      .stDeployButton {display:none;}

      /* Streamlit element customization */
      div.stButton > button {
          background-color: var(--primary);
          color: white;
          border: none;
          padding: 0.5rem 1.5rem;
          border-radius: 5px;
          font-weight: 500;
      }

      div.stButton > button:hover {
          background-color: var(--dark);
      }

      .stProgress > div > div > div > div {
          background-color: var(--primary);
      }
      </style>
      """, unsafe_allow_html=True)

  # Load CSS
  load_css()

  html_code = f'''
            <style>
                #menuToggle {{
                      display: block;
                      position: fixed;
                      bottom:23px;
                      left:30px;
                      z-index: 1;
                      -webkit-user-select: none;
                      user-select: none;
                }}
                # @media (orientation: portrait) {{
                #         #menuToggle {{
                #             bottom:100px;
                #         }}
                # }}
                # @supports (-webkit-appearance: none) and (not (overflow:-webkit-marquee)) {{
                #         #menuToggle {{
                #             bottom:97px;
                #         }}
                # }}
                #menuToggle a {{
                    text-decoration: none;
                    color: white;
                    transition: color 0.3s ease;
                }}
                #menuToggle a:hover {{
                    color: rgb(236,194,12);
                }}
                #menuToggle input {{
                    display: block;
                    width: 65px;
                    height: 65px;
                    position: absolute;
                    top: -7px;
                    left: -5px;
                    cursor: pointer;
                    opacity: 0; /* hide this */
                    z-index: 2; /* and place it over the hamburger */
                    -webkit-touch-callout: none;
                }}
                #menuToggle .float2 {{
                    display: block;
                    width: 33px;
                    height: 4px;
                    margin-bottom: 5px;
                    position: relative;
                    background: rgb(26,34,44);
                    border-radius: 3px;
                    z-index: 1;
                    transform-origin: 4px 0px;
                    transition: transform 0.5s cubic-bezier(0.77,0.2,0.05,1.0),
                              background 0.5s cubic-bezier(0.77,0.2,0.05,1.0),
                              opacity 0.55s ease;
                }}
                #menuToggle .float:first-child {{
                    transform-origin: 0% 0%;
                }}
                #menuToggle .float:nth-last-child(2) {{
                    transform-origin: 0% 100%;
                }}
                #menuToggle input:checked ~ span {{
                    opacity: 1;
                    transform: rotate(45deg) translate(-2px, -1px);
                    background: white;
                }}
                #menuToggle input:checked ~ span:nth-last-child(3) {{
                    opacity: 0;
                    transform: rotate(0deg) scale(0.2, 0.2);
                }}
                #menuToggle input:checked ~ span:nth-last-child(2) {{
                    transform: rotate(-45deg) translate(0, -1px);
                }}
                #menu {{
                display: flex;
                    flex-direction: row;
                    justify-content: flex-end;
                    align-items: center;
                    border-bottom-right-radius: 55px;
                    border-top-right-radius: 55px;
                    position: absolute;
                    width: 400px;
                    margin: -90px 0 0 -50px;
                    padding: 20px;
                    # padding-top: 125px;
                    background: rgb(26,34,44);
                    list-style-type: none;
                    -webkit-font-smoothing: antialiased;
                    /* to stop flickering of text in safari */
                    transform-origin: 0% 0%;
                    transform: translate(-100%, 0);
                    transition: transform 0.5s cubic-bezier(0.77,0.2,0.05,1.0);
                    }}

                #menu li
                {{
                    padding: 10px 0;
                    font-size: 22px;
                }}
                #menuToggle input:checked ~ ul {{
                    transform: none;
                }}

                .box_keywords {{
                    display: none;
                }}

                #menuToggle .float {{
                    # position:fixed;
                    width:65px;
                    height:65px;
                    # bottom:20px;
                    # left:20px;
                    background-color:#2d78c9;
                    color:#FFF;
                    border-radius:50px;
                    text-align:center;
                    box-shadow: 2px 2px 3px rgb(0 0 0 / 0.2);
                    # transition: transform .2s; /* Animation */
                    margin-left: 20px;
                }}

                #menuToggle .float2 {{
                    # position:fixed;
                    width:65px;
                    height:65px;
                    # bottom:20px;
                    # left:20px;
                    background-color:#2d78c9;
                    color:#FFF;
                    border-radius:50px;
                    text-align:center;
                    box-shadow: 0px 0px 14px rgb(0 0 0 / 0.92);
                    # transition: transform .2s; /* Animation */
                }}

                .float:hover {{
                    background-color:#ffffff;
                }}

                .float img {{
                    width: 55px;
                    height: 55px;
                    margin-top:5px;
                }}
            </style>


            <nav role="navigation">
                <div id="menuToggle">
                    <input type="checkbox" />
                        <img src="data:image/{img_format_button};base64,{bin_str_button}" class="float2"/>
                        <ul id="menu">
                                <a href="https://t.me/thegiova" target="_blank" class="float">
                                <img src="data:image/{img_format_telegram};base64,{bin_str_telegram}" />
                                </a>
                                <a href="https://api.whatsapp.com/send?phone=3494346732&text=Ciao," target="_blank" class="float">
                                <img src="data:image/{img_format_whatsapp};base64,{bin_str_whatsapp}" />
                                </a>
                                <a href="{target_url_mail}" class="float">
                                <img src="data:image/{img_format_mail};base64,{bin_str_mail}" />
                                </a>
                        </ul>
                </div>
            </nav>

            '''
  st.markdown(html_code, unsafe_allow_html=True)
