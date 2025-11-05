# app.py
import streamlit as st
import cv2
import time
from detector import PlasticBottleDetector
from utils import estimate_bottle_weight, calculate_bottle_reward
from notify import send_email, send_sms   # 👈 Import the email/SMS sender

# Streamlit setup
st.set_page_config(page_title="Smart RVM", page_icon="♻", layout="wide")

st.markdown("<h1 style='text-align:center; color:#2E8B57;'>♻ Smart Waste Management System</h1>", unsafe_allow_html=True)
st.markdown("---")

# Initialize session variables
if "page" not in st.session_state:
    st.session_state.page = "register"
if "user" not in st.session_state:
    st.session_state.user = None
if "total_reward" not in st.session_state:
    st.session_state.total_reward = 0

# ------------------ NAVIGATION FUNCTION ------------------
def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# ------------------ PAGE 1: REGISTRATION ------------------
if st.session_state.page == "register":
    st.subheader("👤 User Registration")

    name = st.text_input("Full Name")
    phone = st.text_input("Mobile Number")
    email = st.text_input("Email Address")

    if st.button("✅ Register"):
        if name and phone and email:
            st.session_state.user = {"name": name, "phone": phone, "email": email}
            st.session_state.total_reward = 0
            st.success(f"🎉 Welcome, {name}! Registration successful.")
            st.toast("Redirecting to Bottle Scanning...", icon="🔄")
            time.sleep(1)
            go_to("scan")
        else:
            st.error("Please fill all fields before registering.")

# ------------------ PAGE 2: BOTTLE SCANNING ------------------
elif st.session_state.page == "scan":
    user = st.session_state.user
    if not user:
        st.warning("⚠️ Please register first.")
        go_to("register")
    else:
        st.subheader(f"🧴 Bottle Scanning for {user['name']}")
        st.info("📸 Place bottles one by one. Auto-stops after 30 seconds of no detection.")

        total_bottles = 0
        total_reward = 0
        detector = PlasticBottleDetector("models/plastic_detector.pt")

        cap = cv2.VideoCapture(0)
        stframe = st.empty()
        progress = st.progress(0)
        start_time = time.time()
        last_detection = time.time()

        while True:
            ret, frame = cap.read()
            if not ret:
                st.warning("Camera not accessible.")
                break

            frame, count = detector.detect(frame)
            stframe.image(frame, channels="BGR")

            if count > 0:
                for _ in range(count):
                    total_bottles += 1
                    weight = estimate_bottle_weight()
                    reward = calculate_bottle_reward(weight)
                    total_reward += reward
                    st.session_state.total_reward += reward
                    st.success(f"🎉 Bottle #{total_bottles}: {weight}g → +₹{reward}")
                    last_detection = time.time()
                    time.sleep(2)

            progress.progress(min((time.time() - start_time) / 30, 1.0))

            if time.time() - last_detection > 30:
                st.warning("⏳ No bottles detected for 30 seconds. Auto-stopping.")
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                st.info("🛑 Manual stop triggered.")
                break

        cap.release()
        cv2.destroyAllWindows()

        total_weight = total_bottles * 25
        st.metric("Total Bottles", total_bottles)
        st.metric("Total Weight (g)", total_weight)
        st.metric("Reward Earned (₹)", total_reward)
        st.success(f"💰 Cumulative Balance: ₹{st.session_state['total_reward']}")

        # -------- Send Email + SMS --------
        if total_bottles > 0:
            email_subject = "Smart Waste Management - Transaction Summary"
            email_body = f"""
Hello {user['name']},

Your recycling transaction is successful! ♻

📦 Bottles Scanned: {total_bottles}
⚖️ Total Weight: {total_weight}g
💵 Reward Credited: ₹{total_reward}

Thank you for helping make our planet cleaner! 🌱
-- Smart Waste Management System
"""

            sms_text = f"Hi {user['name']}, your recycling was successful! ₹{total_reward} credited for {total_bottles} bottles. ♻"

            st.info("📤 Sending transaction confirmation...")

            email_sent = send_email(user['email'], email_subject, email_body)
            sms_sent = send_sms(user['phone'], sms_text)

            if email_sent:
                st.success(f"📩 Email sent to {user['email']}")
            else:
                st.warning("⚠️ Email sending failed.")

            if sms_sent:
                st.success(f"📱 SMS sent to {user['phone']}")
            else:
                st.warning("⚠️ SMS sending failed.")

        # ✅ Redirect to Reward Summary
        st.toast("Redirecting to Reward Summary...", icon="📊")
        time.sleep(4)
        go_to("summary")

# ------------------ PAGE 3: REWARD SUMMARY ------------------
elif st.session_state.page == "summary":
    user = st.session_state.user
    if not user:
        st.warning("⚠️ Please register first.")
        go_to("register")
    else:
        st.subheader("📊 Reward Summary")
        st.write(f"👤 Name: **{user['name']}**")
        st.write(f"📱 Phone: **{user['phone']}**")
        st.write(f"📧 Email: **{user['email']}**")

        st.metric("Cumulative Reward (₹)", st.session_state.total_reward)
        st.info("Thank you for recycling responsibly! 🌱")

        if st.button("↩ Back to Registration"):
            go_to("register")

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align:center; color:gray;'>Developed by <b>Akshay Lanjewar</b> | Smart RVM System</p>",
            unsafe_allow_html=True
        )
