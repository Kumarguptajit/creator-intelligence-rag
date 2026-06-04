"use client";

import { useState } from "react";

export default function Home() {
  const [videoA, setVideoA] = useState("");
  const [videoB, setVideoB] = useState("");
  const [response, setResponse] = useState("");

  async function compareVideos() {
    setResponse("Loading...");

    const res = await fetch(
      "http://127.0.0.1:8000/compare",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          video_a_url: videoA,
          video_b_url: videoB,
        }),
      }
    );

    const text = await res.text();

    setResponse(text);
  }

  return (
    <main className="max-w-4xl mx-auto p-10">

      <h1 className="text-3xl font-bold mb-8">
        Creator Intelligence RAG
      </h1>

      <input
        className="border p-3 w-full mb-4"
        placeholder="Video A URL"
        value={videoA}
        onChange={(e) =>
          setVideoA(e.target.value)
        }
      />

      <input
        className="border p-3 w-full mb-4"
        placeholder="Video B URL"
        value={videoB}
        onChange={(e) =>
          setVideoB(e.target.value)
        }
      />

      <button
        onClick={compareVideos}
        className="border px-6 py-3"
      >
        Compare Videos
      </button>

      <div className="mt-8 whitespace-pre-wrap border p-4">
        {response}
      </div>

    </main>
  );
}