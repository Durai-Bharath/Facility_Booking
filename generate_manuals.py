from fpdf import FPDF
import os

OUTPUT_DIR = r"C:\Users\bhara\OneDrive\Desktop\project_intern\manuals"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SYSTEM_NAME = "Anna University Facility Booking System"
UNIVERSITY  = "Anna University"

WHITE  = (255, 255, 255)
TEXT   = (31, 41, 55)
MUTED  = (107, 114, 128)
ACCENT = (99, 102, 241)

LM = "LMARGIN"
NX = "NEXT"


def safe(text):
    return (text
            .replace('—', '--').replace('–', '-')
            .replace('‘', "'").replace('’', "'")
            .replace('•', '-').replace('·', '-'))


class Manual(FPDF):
    def __init__(self, role_label, role_color):
        super().__init__()
        self.role_label = role_label
        self.role_color = role_color
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(20, 20, 20)

    def header(self):
        r, g, b = self.role_color
        self.set_fill_color(r, g, b)
        self.rect(0, 0, 210, 14, 'F')
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 9)
        self.set_y(4)
        self.cell(0, 6, safe(f"{SYSTEM_NAME}  |  {self.role_label} Manual"), align="C")
        self.set_text_color(*TEXT)
        self.ln(12)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*MUTED)
        self.cell(0, 8, safe(f"Page {self.page_no()} / {{nb}}  --  {UNIVERSITY}"), align="C")

    def cover(self, role_label, subtitle):
        self.add_page()
        r, g, b = self.role_color
        self.set_fill_color(r, g, b)
        self.rect(0, 0, 210, 82, 'F')
        self.set_y(18)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 24)
        self.multi_cell(0, 11, safe(SYSTEM_NAME), align="C", new_x=LM, new_y=NX)
        self.set_font("Helvetica", "", 13)
        self.multi_cell(0, 8, safe(UNIVERSITY), align="C", new_x=LM, new_y=NX)
        self.ln(4)
        self.set_font("Helvetica", "B", 20)
        self.multi_cell(0, 10, safe(f"{role_label} User Manual"), align="C", new_x=LM, new_y=NX)
        self.set_font("Helvetica", "", 11)
        self.set_text_color(220, 220, 255)
        self.multi_cell(0, 7, safe(subtitle), align="C", new_x=LM, new_y=NX)
        self.set_text_color(*TEXT)
        self.set_y(92)

    def section(self, title):
        self.ln(4)
        r, g, b = self.role_color
        self.set_fill_color(r, g, b)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 12)
        self.multi_cell(0, 8, safe(f"  {title}"), fill=True, new_x=LM, new_y=NX)
        self.set_text_color(*TEXT)
        self.ln(2)

    def sub(self, title):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*ACCENT)
        self.multi_cell(0, 7, safe(title), new_x=LM, new_y=NX)
        self.set_text_color(*TEXT)

    def body(self, text):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 5.5, safe(text), new_x=LM, new_y=NX)
        self.ln(1)

    def bullets(self, items):
        self.set_font("Helvetica", "", 10)
        for item in items:
            self.set_x(self.l_margin + 4)
            self.multi_cell(0, 5.5, safe(f"- {item}"), new_x=LM, new_y=NX)
        self.ln(1)

    def steps(self, items):
        self.set_font("Helvetica", "", 10)
        for i, item in enumerate(items, 1):
            self.set_x(self.l_margin + 4)
            self.multi_cell(0, 5.5, safe(f"{i}. {item}"), new_x=LM, new_y=NX)
        self.ln(1)

    def info_box(self, text, color=(230, 240, 255)):
        self.set_fill_color(*color)
        self.set_font("Helvetica", "I", 9.5)
        self.multi_cell(0, 5.5, safe(f"  {text}"), fill=True, new_x=LM, new_y=NX)
        self.ln(2)

    def build_pdf(self, filename):
        self.alias_nb_pages()
        self._build()
        path = os.path.join(OUTPUT_DIR, filename)
        self.output(path)
        print(f"  Saved: {path}")


# ==================== STUDENT ====================
class StudentManual(Manual):
    def __init__(self):
        super().__init__("Student", (75, 85, 99))

    def _build(self):
        self.cover("Student", "View your timetable and track your schedule")

        self.section("1. Overview")
        self.body(
            "The Student role provides read-only access to the facility booking system. "
            "As a student, you can view your personal timetable for the current day, "
            "see which rooms, labs, and projectors are assigned to each period, and "
            "check holiday notifications. You cannot book or free any facilities."
        )

        self.section("2. Login")
        self.sub("How to Log In")
        self.steps([
            "Open the application in your browser.",
            "Enter your Student User ID (provided by your admin) in the User ID field.",
            "Enter your password.",
            "Click the Login button.",
            "You will be redirected to the Home page.",
        ])
        self.info_box(
            "Note: If you forget your password, contact your system administrator. "
            "Password reset is not self-service."
        )

        self.section("3. Home Page")
        self.body(
            "After logging in you land on the Home page, which shows your user ID and role badge. "
            "The hamburger menu (top-left corner) opens the sidebar navigation."
        )
        self.sub("Sidebar Menu for Student")
        self.bullets([
            "Home -- Returns to the welcome screen.",
            "My Timetable -- Shows today's 8 periods with room/lab/projector assignments.",
            "Messages -- View system notifications.",
        ])

        self.section("4. My Timetable")
        self.body(
            "The timetable page shows today's date and all 8 class periods. "
            "Each period card is colour-coded:"
        )
        self.bullets([
            "Green card -- Period is FREE (no booking).",
            "Red card -- Period is OCCUPIED (a room or lab is assigned).",
        ])
        self.sub("Information shown per period card")
        self.bullets([
            "Period number (1-8)",
            "Time slot (e.g. 08:30 -- 09:20)",
            "Status: Occupied or Free",
            "Staff name (if occupied)",
            "Course code (if occupied)",
            "Room or Lab name (if assigned)",
            "Projector name (if booked)",
        ])
        self.info_box(
            "Weekends and Holidays: On weekends or declared holidays the timetable page "
            "shows a notice instead of period cards. No bookings are possible on those days."
        )
        self.sub("Read-only Access")
        self.body(
            "Students cannot Book or Free any period. The action buttons visible to other "
            "roles (Book, Free, + Projector) are hidden for the Student role."
        )

        self.section("5. Messages")
        self.body(
            "The Messages section lets you receive system notifications. "
            "Navigate via Sidebar > Messages."
        )

        self.section("6. Sign Out")
        self.steps([
            "Open the sidebar (hamburger icon, top-left).",
            "Scroll to the bottom of the menu.",
            "Click Sign Out.",
            "You will be returned to the Login page.",
        ])
        self.info_box(
            "Always sign out on shared or public computers to protect your account."
        )

        self.section("7. Frequently Asked Questions")
        self.sub("Q: I cannot see any periods on my timetable.")
        self.body(
            "A: Your admin may not have set up your timetable yet. "
            "Contact your department administrator."
        )
        self.sub("Q: Today is a weekday but the timetable shows a holiday notice.")
        self.body(
            "A: The admin has marked today as a holiday. Bookings are disabled for that day."
        )
        self.sub("Q: I need to book a room for a study group.")
        self.body(
            "A: Students cannot book rooms directly. "
            "Ask your Student Representative or a Faculty member."
        )


# ==================== STUDENT REPRESENTATIVE ====================
class StudentRepManual(Manual):
    def __init__(self):
        super().__init__("Student Representative", (124, 58, 237))

    def _build(self):
        self.cover("Student Representative",
                   "Book rooms, labs, projectors, and halls on behalf of students")

        self.section("1. Overview")
        self.body(
            "The Student Representative (student_rep) role has limited booking capabilities. "
            "You can book rooms, labs, and projectors for your own timetable periods, "
            "and request hall bookings for events. Bookings can be made up to 6 days in advance "
            "(faculty and secretaries can book up to 60 days ahead). "
            "You also have access to the Messages feature."
        )

        self.section("2. Login")
        self.steps([
            "Open the application in your browser.",
            "Enter your Student Rep User ID and password.",
            "Click Login -- you will reach the Home page.",
        ])

        self.section("3. Sidebar Navigation")
        self.bullets([
            "Home -- Welcome screen.",
            "Facilitywise Booking -- Browse all rooms, labs, projectors by date.",
            "My Bookings -- View and manage your own period-based bookings.",
            "Halls -- Request a hall for an event.",
            "Messages -- View notifications and messages.",
        ])

        self.section("4. My Bookings (Period-Based)")
        self.body(
            "This page shows your 8 periods for today. You can book a room or lab for a free "
            "period, and add a projector to an already-occupied period."
        )
        self.sub("Booking a Room or Lab")
        self.steps([
            "Go to Sidebar > My Bookings.",
            "Find a GREEN (Free) period card.",
            "Click the Book button on that card.",
            "You are redirected to the Room Listing page -- select an available room or lab.",
            "Confirm the booking.",
        ])
        self.sub("Adding a Projector")
        self.steps([
            "On a RED (Occupied) period card that has no projector yet, click + Projector.",
            "You are redirected to the Projector Listing page.",
            "Select an available projector and confirm.",
        ])
        self.sub("Freeing a Period")
        self.steps([
            "On an OCCUPIED period card, click the Free button.",
            "The room/lab is released and the period becomes Free.",
        ])
        self.info_box(
            "You can only act on periods whose start time is in the future or currently ongoing. "
            "Past periods are locked (action buttons are hidden)."
        )

        self.section("5. Facilitywise Booking")
        self.body(
            "This page shows all rooms, labs, and projectors with their availability per period "
            "for a selected date. Student Reps can only view dates within the next 6 days."
        )
        self.steps([
            "Go to Sidebar > Facilitywise Booking.",
            "Select a date from the calendar (only working days up to 6 days ahead).",
            "Optionally filter by Facility Type (KP Room, Dept Room, Lab, Projector).",
            "Browse period slots -- Free slots show a Book button.",
            "Click Book on a free, future slot to reserve that facility.",
        ])
        self.info_box("Slots in the past (greyed out) cannot be booked.")

        self.section("6. Hall Booking")
        self.body(
            "Halls can be requested for events. A Student Rep can book up to 6 days in advance. "
            "A PDF supporting document is required for all hall requests."
        )
        self.steps([
            "Go to Sidebar > Halls.",
            "Select a date from the date tabs at the top.",
            "Click on FREE time slots (15-min intervals) to select your booking window.",
            "Slots must be continuous -- you cannot select non-adjacent slots.",
            "Enter an Event Name in the text field.",
            "Upload a supporting PDF document (max 2 MB).",
            "Click Confirm Booking.",
            "Your request is submitted to the admin for approval.",
        ])
        self.info_box(
            "IMPORTANT: Hall booking requests require admin approval. "
            "You will receive a notification once accepted or rejected."
        )

        self.section("7. Messages")
        self.body("Navigate to Sidebar > Messages to view notifications.")

        self.section("8. Sign Out")
        self.steps(["Open the sidebar.", "Click Sign Out at the bottom."])

        self.section("9. Frequently Asked Questions")
        self.sub("Q: The Book button does not appear on a slot.")
        self.body("A: The slot may already be booked or the date/time is in the past.")
        self.sub("Q: My hall booking is not approved yet.")
        self.body("A: Hall requests require admin approval. Please wait or contact the admin.")
        self.sub("Q: Can I book for next week?")
        self.body(
            "A: Student Reps can book up to 6 days in advance. "
            "Faculty and secretaries have a 60-day window."
        )


# ==================== FACULTY ====================
class FacultyManual(Manual):
    def __init__(self):
        super().__init__("Faculty", (37, 99, 235))

    def _build(self):
        self.cover("Faculty",
                   "Manage your periods, book facilities, and request halls")

        self.section("1. Overview")
        self.body(
            "Faculty members have a comprehensive booking experience. You can manage your "
            "period-based bookings (book rooms, labs, add projectors, free periods), browse "
            "facilities across dates up to 60 days ahead, and request hall bookings for events. "
            "You also have access to the Messages feature."
        )

        self.section("2. Login")
        self.steps([
            "Open the application in your browser.",
            "Enter your Faculty User ID and password.",
            "Click Login.",
        ])

        self.section("3. Sidebar Navigation")
        self.bullets([
            "Home -- Welcome screen.",
            "Facilitywise Booking -- Browse all rooms, labs, projectors by date (up to 60 days).",
            "Halls -- Request a hall for an event (up to 60 days ahead).",
            "Messages -- View notifications.",
        ])

        self.section("4. Facilitywise Booking")
        self.body(
            "This is the primary booking interface for faculty. It shows all rooms, labs, "
            "and projectors with their per-period availability for any working day up to 60 days."
        )
        self.steps([
            "Go to Sidebar > Facilitywise Booking.",
            "Pick a date from the calendar -- all working days up to 60 days are available.",
            "Use the Facility Type dropdown to filter: All, KP Room, Dept Room, Lab, Projector.",
            "Each facility card shows 8 period slots -- red (booked) or white (free).",
            "Click the Book button on a white (free) future slot to book it for yourself.",
            "A confirmation alert appears after successful booking.",
        ])
        self.sub("Facility Type Colour Coding")
        self.bullets([
            "Blue border -- Room (KP or Department)",
            "Purple border -- Lab",
            "Yellow border -- Projector",
        ])

        self.section("5. Hall Booking")
        self.body(
            "Faculty can request halls up to 60 days ahead. "
            "A PDF supporting document is required."
        )
        self.steps([
            "Go to Sidebar > Halls.",
            "Select a date from the date tabs.",
            "Click on consecutive 15-minute time slots to select your booking window.",
            "Enter an Event Name.",
            "Upload a supporting PDF (max 2 MB).",
            "Click Confirm Booking.",
            "Wait for admin approval.",
        ])
        self.info_box(
            "Slots must be continuous. Selecting non-adjacent slots will show an error "
            "and the Confirm Booking button will be disabled."
        )

        self.section("6. Rooms and Projectors")
        self.sub("Room Listing")
        self.body(
            "The Room Listing page (/rooms) shows all available rooms and labs for a selected "
            "period. It is reached via the booking flow from Facilitywise Booking."
        )
        self.sub("Projector Listing")
        self.body(
            "The Projector Listing page (/projectorlisting) shows available projectors. "
            "Access it when adding a projector to an already-booked period."
        )

        self.section("7. Messages")
        self.body("Go to Sidebar > Messages to view notifications related to your bookings.")

        self.section("8. Sign Out")
        self.steps(["Open the sidebar.", "Click Sign Out."])

        self.section("9. Frequently Asked Questions")
        self.sub("Q: I booked the wrong room. How do I undo it?")
        self.body(
            "A: Use Facilitywise Booking, locate your booking on the same date, and click Free "
            "(if visible). Contact the admin if the slot is locked."
        )
        self.sub("Q: My hall booking was rejected.")
        self.body("A: Check Messages for the admin's reason. Resubmit with updated details.")
        self.sub("Q: Can I see what rooms other faculty have booked?")
        self.body(
            "A: Yes -- the Facilitywise Booking page shows all booked slots with "
            "the booker's user ID."
        )


# ==================== SECRETARY ====================
class SecretaryManual(Manual):
    def __init__(self):
        super().__init__("Secretary", (217, 119, 6))

    def _build(self):
        self.cover("Secretary",
                   "Book facilities and request halls and auditoriums")

        self.section("1. Overview")
        self.body(
            "The Secretary role has the same facility booking capabilities as Faculty, "
            "plus exclusive access to Auditorium booking requests. Secretaries can book "
            "rooms, labs, and projectors via Facilitywise Booking, request halls, and "
            "submit auditorium booking requests for large events."
        )

        self.section("2. Login")
        self.steps([
            "Open the application in your browser.",
            "Enter your Secretary User ID and password.",
            "Click Login.",
        ])

        self.section("3. Sidebar Navigation")
        self.bullets([
            "Home -- Welcome screen.",
            "Facilitywise Booking -- Browse and book rooms, labs, projectors (up to 60 days).",
            "Halls -- Request a hall for an event.",
            "Auditorium -- Submit an auditorium booking request (Secretary exclusive).",
            "Messages -- View notifications.",
        ])

        self.section("4. Facilitywise Booking")
        self.body("Identical to the Faculty experience.")
        self.steps([
            "Go to Sidebar > Facilitywise Booking.",
            "Select a date (up to 60 days ahead).",
            "Filter by facility type if needed.",
            "Click Book on a free, future period slot.",
        ])

        self.section("5. Hall Booking")
        self.body("Identical to the Faculty experience.")
        self.steps([
            "Sidebar > Halls > Select date.",
            "Click consecutive time slots.",
            "Enter Event Name and upload PDF.",
            "Click Confirm Booking and await admin approval.",
        ])

        self.section("6. Auditorium Booking Request  (Secretary Exclusive)")
        self.body(
            "Secretaries are the only role that can request auditorium bookings. "
            "Two auditoriums are available:"
        )
        self.bullets([
            "Vivekananda Auditorium -- Block A, Capacity: 500, "
            "Features: AC, Projector, Sound System",
            "Tag Auditorium -- Block B, Capacity: 300, Features: Projector, Sound System",
        ])
        self.sub("How to Submit an Auditorium Request")
        self.steps([
            "Go to Sidebar > Auditorium.",
            "Click on the auditorium card you want to book (it will be highlighted).",
            "Date -- must be at least tomorrow, up to 30 days ahead.",
            "Start Time and End Time (end must be after start).",
            "Event Name (required).",
            "Additional Information (optional).",
            "Upload a supporting PDF (max 2 MB, PDF format only).",
            "Click Submit Request.",
            "A green confirmation banner will appear: Request Submitted!",
        ])
        self.info_box(
            "Auditorium requests require admin approval. "
            "Do not submit duplicate requests while one is pending."
        )

        self.section("7. Messages")
        self.body("Go to Sidebar > Messages for booking notifications and admin communications.")

        self.section("8. Sign Out")
        self.steps(["Open the sidebar.", "Click Sign Out."])

        self.section("9. Frequently Asked Questions")
        self.sub("Q: I submitted an auditorium request but received no confirmation email.")
        self.body("A: The system sends in-app notifications only. Check the Messages section.")
        self.sub("Q: Can I book the auditorium for the same day?")
        self.body("A: No. The minimum lead time is one day. Same-day booking is not allowed.")
        self.sub("Q: I uploaded the wrong PDF.")
        self.body("A: You must resubmit the entire form. There is no edit after submission.")


# ==================== ADMIN ====================
class AdminManual(Manual):
    def __init__(self):
        super().__init__("Admin", (220, 38, 38))

    def _build(self):
        self.cover("Admin",
                   "Full system control: users, facilities, timetables, and approvals")

        self.section("1. Overview")
        self.body(
            "The Admin role has unrestricted access to all management functions: "
            "register and delete users, manage facilities, build timetables, "
            "manage enrollment, configure holidays and special working days, "
            "approve or reject hall and auditorium requests, view booking history, "
            "and monitor real-time facility usage via the Dashboard."
        )

        self.section("2. Login")
        self.steps([
            "Open the application in your browser.",
            "Enter your Admin User ID and password.",
            "Click Login.",
        ])

        self.section("3. Sidebar Navigation")
        self.bullets([
            "Home -- Welcome screen.",
            "Requests -- Approve / reject pending hall and auditorium requests.",
            "History -- View complete booking history.",
            "Dashboard -- Real-time facility usage by date.",
            "Facilities -- Add, edit, or delete facility entries.",
            "Enrollment -- Enroll users in courses.",
            "Timetable -- Build timetables, add holidays, manage special working days.",
            "Register -- Create users individually or via CSV bulk import; delete users.",
        ])

        self.section("4. User Management (Register)")
        self.sub("Register a Single User")
        self.steps([
            "Sidebar > Register > Register User tab.",
            "Enter User ID, Password, Email.",
            "Select a Role: student, student_rep, faculty, secretary, admin.",
            "Click Register User.",
        ])
        self.sub("Bulk Register via CSV")
        self.steps([
            "Sidebar > Register > Bulk Register tab.",
            "Prepare a CSV file with columns: userId,password,role,email",
            "Click Upload CSV File or paste the CSV text into the textarea.",
            "Click Parse and Preview -- a table shows the parsed records.",
            "Fix any errors shown, then re-parse.",
            "Click Register N Users to submit.",
        ])
        self.info_box("Valid roles in CSV: student, student_rep, faculty, secretary, admin")
        self.sub("Manage / Delete Users")
        self.steps([
            "Sidebar > Register > Manage Users tab.",
            "Filter by role if needed.",
            "Click Delete next to a single user -- removes the user and ALL their data.",
            "Use checkboxes + Delete Selected for bulk deletion.",
        ])
        self.info_box(
            "WARNING: Deleting a user permanently removes their timetable, bookings, "
            "enrollment, and requests. This action cannot be undone."
        )

        self.section("5. Facility Management")
        self.body("Facilities include Rooms, Labs, Projectors, and Halls.")
        self.sub("Add a Facility")
        self.steps([
            "Sidebar > Facilities > click + Add Facility.",
            "Enter the Facility Name.",
            "Select Type: room, lab, projector, or hall.",
            "Check or uncheck Bookable.",
            "Click Add.",
        ])
        self.sub("Edit Bookable Status")
        self.steps([
            "Click Edit Bookable to enter edit mode.",
            "Find the facility and click Edit.",
            "Toggle the Bookable checkbox and click Save.",
        ])
        self.sub("Delete a Facility")
        self.steps([
            "Click Delete Facility to enter delete mode.",
            "Click Delete next to the facility and confirm.",
        ])

        self.section("6. Enrollment Management")
        self.body(
            "Enrollment links a user to a set of courses. "
            "This is required before building a timetable for that user."
        )
        self.steps([
            "Sidebar > Enrollment.",
            "Enter the User ID to enroll.",
            "In the Add Course section enter Course Code, Course Name, Staff Name.",
            "Check Lab if the course uses a lab instead of a room.",
            "Click Add Course -- the course appears in the preview table.",
            "Add as many courses as needed; Edit or Remove any before submitting.",
            "Click Submit Enrollment.",
        ])
        self.sub("Delete Enrollment")
        self.body(
            "In the All Enrollments section, click Delete next to a user "
            "to remove their entire enrollment record."
        )

        self.section("7. Timetable Management")
        self.body(
            "The Timetable page has three tabs: "
            "Build Timetable, Special Working Days, Holidays."
        )
        self.sub("7a. Build Timetable")
        self.steps([
            "Sidebar > Timetable > Build Timetable tab.",
            "Select a User from the dropdown (only enrolled users appear).",
            "Optionally set a Default Room and Default Lab.",
            "Drag a course badge from the course list onto a period cell (Mon-Fri, P1-P8).",
            "To edit room/lab for a specific period, click Edit on that cell.",
            "To remove an assignment, click the X button.",
            "Click Submit Timetable when done.",
        ])
        self.info_box(
            "Each timetable covers 5 days x 8 periods = 40 cells. "
            "Unassigned cells are marked Free."
        )
        self.sub("7b. Special Working Days")
        self.steps([
            "Timetable > Special Working Days tab.",
            "Select a Saturday date (only Saturdays are allowed).",
            "Choose which day timetable it follows (or leave blank for open/no-timetable).",
            "Add an optional label.",
            "Click Add Special Day.",
        ])
        self.sub("7c. Holidays / Off Days")
        self.steps([
            "Timetable > Holidays / Off Days tab.",
            "Toggle Single Day or Date Range mode.",
            "Select the date(s) and optionally add a label.",
            "Click Mark as Holiday.",
        ])
        self.info_box(
            "On a declared holiday, booking pages show a holiday banner "
            "and all booking actions are disabled."
        )

        self.section("8. Requests -- Approve / Reject")
        self.sub("Hall Requests")
        self.steps([
            "Sidebar > Requests.",
            "Under Pending Hall Requests, use filter buttons (All / Faculty / Student Rep / Secretary).",
            "Review: Hall, User, Role, Date, Event, Start, End.",
            "Click View PDF to check the supporting document.",
            "Click the green checkmark to Accept or the red X to Reject.",
        ])
        self.sub("Auditorium Requests")
        self.steps([
            "Scroll down to Pending Auditorium Requests.",
            "Review details and click View PDF.",
            "Click Accept or Reject.",
        ])
        self.info_box(
            "Accepting marks the slot as booked. Rejecting frees it for others."
        )

        self.section("9. Dashboard -- Facility Usage")
        self.steps([
            "Sidebar > Dashboard.",
            "Select a date from the inline calendar.",
            "Filter by Facility Type: All, KP Room, Dept Room, Lab, Projector, Hall.",
            "Red slot = booked (shows booker's user ID), white slot = free.",
            "For a future booked slot, click Free to force-release it.",
        ])

        self.section("10. History")
        self.body("Navigate to Sidebar > History to review past booking activity.")

        self.section("11. Sign Out")
        self.steps(["Open the sidebar.", "Click Sign Out."])

        self.section("12. Frequently Asked Questions")
        self.sub("Q: Can I change a user's role after creation?")
        self.body("A: Not through the UI. Delete the user and re-register with the correct role.")
        self.sub("Q: A hall shows as occupied but the event was cancelled.")
        self.body("A: Go to Dashboard, find the slot, and click Free to release it manually.")
        self.sub("Q: How do I add a compensatory working Saturday?")
        self.body(
            "A: Timetable > Special Working Days > select the Saturday, "
            "choose which day timetable it follows, and save."
        )
        self.sub("Q: What data is deleted when I delete a user?")
        self.body(
            "A: All associated data is permanently removed: timetable, bookings, "
            "enrollments, and pending requests."
        )


# ==================== Generate ====================
print("Generating manuals...")
StudentManual().build_pdf("student_manual.pdf")
StudentRepManual().build_pdf("student_rep_manual.pdf")
FacultyManual().build_pdf("faculty_manual.pdf")
SecretaryManual().build_pdf("secretary_manual.pdf")
AdminManual().build_pdf("admin_manual.pdf")
print(f"\nAll 5 manuals saved to:\n{OUTPUT_DIR}")
