import { useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';

export default function Sidebar() {

  const stored = localStorage.getItem('user');
  const user = stored ? JSON.parse(stored) : null;

  const navigate = useNavigate();
  const location = useLocation();

  const [open, setOpen] = useState(true);

  const handleSignOut = () => {

    localStorage.removeItem('user');

    localStorage.removeItem('token');

    navigate('/');

  };

  if (!user) return null;

  const isFaculty = user.role === 'faculty';

  const isSecretary = user.role === 'secretary';

  const isStudentRep = user.role === 'student_rep';

  const isStudent = user.role === 'student';

  const isAdmin = user.role === 'admin';



  return (

    <>

      {/* Open Button */}

      {

        !open && (

          <button

            onClick={() => setOpen(true)}

            className="

            fixed

            top-5

            left-5

            z-[950]

            text-3xl

            font-bold

            text-blue-600

            hover:text-blue-700

            transition-all

            "

          >

            ☰

          </button>

        )

      }



      {/* Overlay */}

      {

        open && (

          <div

            className="fixed inset-0 bg-black/20 z-[800]"

            onClick={() => setOpen(false)}

          />

        )

      }



      {/* Sidebar */}

      <nav

        className={`

        fixed

        top-[72px]

        left-0

        h-[calc(100vh-72px)]

        w-52

        bg-slate-900

        shadow-xl

        z-[900]

        px-4

        py-5

        flex

        flex-col

        transition-all

        duration-300

        ${open ? 'translate-x-0' : '-translate-x-full'}

        `}

      >



        {/* Hamburger */}

        <div className="mb-6">

          <button

            onClick={() => setOpen(false)}

            className="

            text-3xl

            font-bold

            text-blue-600

            hover:text-blue-700

            transition-all

            "

          >

            ☰

          </button>

        </div>




        {/* Menu */}

        <ul className="flex flex-col gap-2 flex-1">

          <NavItem

            to="/home"

            current={location.pathname}

          >

            Home

          </NavItem>



          {

            (isFaculty || isSecretary || isStudentRep)

            &&

            <NavItem

              to="/facilitywiseBooking"

              current={location.pathname}

            >

              Facility Booking

            </NavItem>

          }



          {

            isStudentRep

            &&

            <NavItem

              to="/booking"

              current={location.pathname}

            >

              My Bookings

            </NavItem>

          }



          {

            (isFaculty || isSecretary || isStudentRep)

            &&

            <NavItem

              to="/halls"

              current={location.pathname}

            >

              Halls

            </NavItem>

          }



          {

            isSecretary

            &&

            <NavItem

              to="/auditorium"

              current={location.pathname}

            >

              Auditorium

            </NavItem>

          }



          {

            (isFaculty || isSecretary || isStudentRep)

            &&

            <NavItem

              to="/messages"

              current={location.pathname}

            >

              Messages

            </NavItem>

          }



          {

            isStudent

            &&

            <NavItem

              to="/booking"

              current={location.pathname}

            >

              My Timetable

            </NavItem>

          }



          {

            isAdmin &&

            <>

              <NavItem to="/requests" current={location.pathname}>

                Requests

              </NavItem>



              <NavItem to="/history" current={location.pathname}>

                History

              </NavItem>



              <NavItem to="/dashboard" current={location.pathname}>

                Dashboard

              </NavItem>



              <NavItem to="/facilities" current={location.pathname}>

                Facilities

              </NavItem>



              <NavItem to="/enrollment" current={location.pathname}>

                Enrollment

              </NavItem>



              <NavItem to="/timetable" current={location.pathname}>

                Timetable

              </NavItem>



              <NavItem to="/register" current={location.pathname}>

                Register

              </NavItem>

            </>

          }

        </ul>




        {/* Sign Out */}

        <button

          onClick={handleSignOut}

          className="

          mt-auto

          bg-red-500

          hover:bg-red-600

          text-white

          py-3

          rounded-xl

          font-semibold

          transition-all

          shadow-md

          "

        >

          Sign Out

        </button>

      </nav>

    </>

  );

}



function NavItem({

  to,

  children,

  current

}) {

  const active = current === to;

  return (

    <li>

      <Link

        to={to}

        className={`

        block

        px-4

        py-3

        rounded-xl

        font-medium

        transition-all

        ${

          active

          ?

          'bg-blue-600 text-white'

          :

          'text-slate-200 hover:bg-slate-800'

        }

        `}

      >

        {children}

      </Link>

    </li>

  );

}