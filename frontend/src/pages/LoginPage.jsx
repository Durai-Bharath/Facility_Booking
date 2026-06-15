import { useState } from "react";
import { useNavigate } from "react-router-dom";
import logo from "../assets/logo.png";
import api from "../utils/api";

export default function LoginPage({ onLogin }) {

  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleSubmit = async (e) => {

    e.preventDefault();

    if (!userId || !password) {

      setError("Please enter both User ID and Password.");

      return;

    }

    setError("");

    setLoading(true);

    try {

      const { data } = await api.post("/login", {

        userId,

        password

      });

      localStorage.setItem("token", data.token);

      localStorage.setItem(

        "user",

        JSON.stringify({

          userId: data.userId,

          role: data.role

        })

      );

      onLogin({

        userId: data.userId,

        role: data.role

      });

      navigate("/home");

    }

    catch (err) {

      setError(

        err.response?.data?.error ||

        err.response?.data?.message ||

        "Login failed. Please try again."

      );

    }

    finally {

      setLoading(false);

    }

  };

  return (

    <div className="min-h-screen flex">

      {/* LEFT PANEL */}

      <div className="hidden md:flex md:w-1/2 bg-slate-900 text-white flex-col justify-center px-16 relative overflow-hidden">

        <div className="absolute top-0 left-0 h-full w-full">

          <div className="absolute h-72 w-72 rounded-full bg-blue-700 opacity-20 -top-20 -left-20"></div>

          <div className="absolute h-96 w-96 rounded-full bg-indigo-600 opacity-20 bottom-0 right-0"></div>

        </div>

        <div className="relative z-10">

          <img

            src={logo}

            alt="Anna University"

            className="h-24 mb-8"

          />

          <h1 className="text-5xl font-bold">

            Anna University

          </h1>

          <p className="text-2xl mt-4 text-slate-300">

            Facility Booking System

          </p>

          <p className="mt-8 text-lg text-slate-400 leading-8">

            Book and manage university facilities easily and efficiently.

          </p>

          <div className="mt-14 space-y-7">

            <div className="flex items-center gap-4">

              <span className="text-3xl">

                📚

              </span>

              <p className="text-lg">

                Classroom Booking

              </p>

            </div>

            <div className="flex items-center gap-4">

              <span className="text-3xl">

                💻

              </span>

              <p className="text-lg">

                Laboratory Reservation

              </p>

            </div>

            <div className="flex items-center gap-4">

              <span className="text-3xl">

                🎥

              </span>

              <p className="text-lg">

                Projector Booking

              </p>

            </div>

            <div className="flex items-center gap-4">

              <span className="text-3xl">

                🏛

              </span>

              <p className="text-lg">

                Auditorium & Hall Requests

              </p>

            </div>

          </div>

        </div>

      </div>

      {/* RIGHT PANEL */}

      <div className="w-full md:w-1/2 bg-slate-100 flex justify-center items-center">

        <form

          onSubmit={handleSubmit}

          className="

          bg-white

          shadow-2xl

          rounded-3xl

          px-10

          py-10

          w-full

          max-w-md

          "

        >

          <h2 className="text-center text-3xl font-bold text-slate-800">

            Welcome Back 👋

          </h2>

          <p className="text-center text-gray-500 mt-2 mb-8">

            Sign in to continue

          </p>

          <div className="mb-5">

            <label className="block mb-2 font-semibold text-slate-700">

              User ID

            </label>

            <input

              type="text"

              value={userId}

              onChange={(e) => setUserId(e.target.value)}

              placeholder="Enter your User ID"

              className="

              w-full

              border

              border-gray-300

              rounded-xl

              px-4

              py-3

              focus:outline-none

              focus:ring-2

              focus:ring-blue-500

              "

            />

          </div>

          <div className="mb-3">

            <label className="block mb-2 font-semibold text-slate-700">

              Password

            </label>

            <input

              type="password"

              value={password}

              onChange={(e) => setPassword(e.target.value)}

              placeholder="Enter your password"

              className="

              w-full

              border

              border-gray-300

              rounded-xl

              px-4

              py-3

              focus:outline-none

              focus:ring-2

              focus:ring-blue-500

              "

            />

          </div>

          <div className="flex justify-end mb-6">

            <button

              type="button"

              className="

              text-blue-600

              hover:text-blue-800

              text-sm

              font-medium

              "

            >

              Forgot Password?

            </button>

          </div>

          {

            error

            &&

            (

              <div className="bg-red-100 text-red-700 rounded-xl p-3 text-center mb-5">

                {error}

              </div>

            )

          }

          <button

            type="submit"

            disabled={loading}

            className="

            w-full

            py-3

            rounded-xl

            bg-gradient-to-r

            from-blue-600

            to-indigo-700

            hover:scale-105

            transition-all

            duration-300

            text-white

            font-semibold

            "

          >

            {

              loading

              ?

              "Signing In..."

              :

              "Sign In"

            }

          </button>

        </form>

      </div>

    </div>

  );

}