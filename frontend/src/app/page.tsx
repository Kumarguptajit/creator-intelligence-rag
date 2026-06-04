"use client";

import { useState } from "react";

export default function Home() {
  const [videoA, setVideoA] = useState("");
  const [videoB, setVideoB] = useState("");
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([
  {
    role: "assistant",
    content: "Paste two videos and click Compare."
  }
]);

  async function compareVideos() {
    setMessages([
      {
        role: "assistant",
        content: "Loading..."
      }
    ]);

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

    setMessages([
      {
        role: "assistant",
        content: text
      }
    ]);
  }

  async function askQuestion() {

    const res = await fetch(
      "http://127.0.0.1:8000/chat",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          question
        })
      }
    );

    const data = await res.json();

    setMessages([
      ...messages,
      {
        role: "user",
        content: question
      },
      {
        role: "assistant",
        content: data.answer
      }
    ]);

    setQuestion("");
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

      <input
        className="border p-3 w-full mt-4"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) =>
          setQuestion(e.target.value)
        }
      />

      <button
        onClick={askQuestion}
        className="border px-6 py-3 mt-4"
      >
        Send
      </button>

      <div className="mt-8 border p-4">

        {messages.map((message, index) => (

          <div
            key={index}
            className="mb-6"
          >

            <strong>
              {message.role}
            </strong>

            <div className="whitespace-pre-wrap">
              {message.content}
            </div>

          </div>

        ))}

      </div>

    </main>
  );
}