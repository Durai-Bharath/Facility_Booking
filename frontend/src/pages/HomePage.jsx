import Banner from '../components/Banner';
import Sidebar from '../components/Sidebar';

export default function HomePage({ user }) {

  const cards = [
    {
      icon: "📚",
      title: "Classrooms",
      count: "25 Available"
    },
    {
      icon: "💻",
      title: "Laboratories",
      count: "12 Available"
    },
    {
      icon: "🎥",
      title: "Projectors",
      count: "7 Available"
    },
    {
      icon: "🏛",
      title: "Auditoriums",
      count: "3 Available"
    }
  ];

  return (

    <div className="min-h-screen bg-gradient-to-br from-slate-100 via-blue-50 to-indigo-100">

      <Banner />

      <Sidebar />

      <div className="pt-28 px-8 md:px-14 ml-16">

        {/* Welcome Section */}

        <div className="mb-10">

          <h1 className="text-4xl font-bold text-slate-800">

            Welcome,

            <span className="text-blue-700 ml-2">

              {user?.userId?.charAt(0).toUpperCase() + user?.userId?.slice(1)} 👋

            </span>

          </h1>

          <p className="text-gray-600 mt-3 text-lg">

            Manage all your university facilities from one place.

          </p>

        </div>


        {/* Dashboard Cards */}

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">

          {

            cards.map((card, index) => (

              <div

                key={index}

                className="

                bg-white

                rounded-3xl

                shadow-xl

                p-8

                hover:scale-105

                hover:shadow-2xl

                transition-all

                duration-300

                cursor-pointer

                "

              >

                <div className="text-5xl">

                  {card.icon}

                </div>

                <h2 className="text-2xl font-bold text-slate-800 mt-5">

                  {card.title}

                </h2>

                <p className="text-gray-500 mt-2">

                  {card.count}

                </p>

              </div>

            ))

          }

        </div>



        {/* Quick Actions */}

        <div

          className="

          bg-white

          rounded-3xl

          shadow-xl

          mt-12

          p-8

          "

        >

          <h2 className="text-2xl font-bold text-slate-800 mb-8">

            Quick Actions

          </h2>


          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">


            <div className="bg-slate-50 rounded-2xl p-6 hover:shadow-lg transition-all">

              <h3 className="text-4xl">

                📚

              </h3>

              <h4 className="font-bold text-xl mt-4">

                Book Classroom

              </h4>

              <p className="text-gray-500 mt-2">

                Create and manage classroom bookings.

              </p>

              <button

                className="

                mt-5

                bg-blue-600

                hover:bg-blue-700

                text-white

                px-5

                py-2

                rounded-xl

                "

              >

                Book Now

              </button>

            </div>




            <div className="bg-slate-50 rounded-2xl p-6 hover:shadow-lg transition-all">

              <h3 className="text-4xl">

                💻

              </h3>

              <h4 className="font-bold text-xl mt-4">

                Book Laboratory

              </h4>

              <p className="text-gray-500 mt-2">

                Reserve laboratories quickly.

              </p>

              <button

                className="

                mt-5

                bg-blue-600

                hover:bg-blue-700

                text-white

                px-5

                py-2

                rounded-xl

                "

              >

                Book Now

              </button>

            </div>




            <div className="bg-slate-50 rounded-2xl p-6 hover:shadow-lg transition-all">

              <h3 className="text-4xl">

                🎥

              </h3>

              <h4 className="font-bold text-xl mt-4">

                Book Projector

              </h4>

              <p className="text-gray-500 mt-2">

                Manage projector availability.

              </p>

              <button

                className="

                mt-5

                bg-blue-600

                hover:bg-blue-700

                text-white

                px-5

                py-2

                rounded-xl

                "

              >

                Book Now

              </button>

            </div>




            <div className="bg-slate-50 rounded-2xl p-6 hover:shadow-lg transition-all">

              <h3 className="text-4xl">

                🏛

              </h3>

              <h4 className="font-bold text-xl mt-4">

                Request Auditorium

              </h4>

              <p className="text-gray-500 mt-2">

                Request halls and auditoriums.

              </p>

              <button

                className="

                mt-5

                bg-blue-600

                hover:bg-blue-700

                text-white

                px-5

                py-2

                rounded-xl

                "

              >

                Request

              </button>

            </div>


          </div>

        </div>


        {/* Footer */}

        <div className="text-center py-10 text-gray-500">

          © 2026 Anna University - Facility Booking System

        </div>

      </div>

    </div>

  );

}