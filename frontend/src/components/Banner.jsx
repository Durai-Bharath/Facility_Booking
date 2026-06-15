export default function Banner() {

  const stored = localStorage.getItem('user');

  const user = stored ? JSON.parse(stored) : null;


  return (

    <header

      className="

      fixed

      top-0

      left-0

      right-0

      h-[72px]

      z-[700]

      bg-white

      shadow-md

      border-b

      border-slate-200

      "

    >

      <div

        className="

        h-full

        flex

        items-center

        justify-end

        px-10

        "

      >


        <div

          className="

          bg-slate-100

          px-6

          py-3

          rounded-2xl

          shadow-sm

          text-center

          "

        >

          <p

            className="

            text-gray-500

            text-xs

            uppercase

            tracking-wide

            "

          >

            Logged in as

          </p>



          <p

            className="

            text-slate-800

            text-2xl

            font-bold

            "

          >

            {

              user?.userId

              ?

              user.userId.charAt(0).toUpperCase()

              +

              user.userId.slice(1)

              :

              'Guest'

            }

          </p>

        </div>


      </div>

    </header>

  );

}