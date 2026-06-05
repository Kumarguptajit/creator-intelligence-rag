"use client";

import { useState } from "react";


export default function Home() {
  const [videoA, setVideoA] = useState("");
  const [videoB, setVideoB] = useState("");
  const [question, setQuestion] = useState("");

  const [videoData, setVideoData] =
    useState<any>(null);

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
        content: "Analyzing videos..."
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
    const contextRes = await fetch(
      "http://127.0.0.1:8000/comparison-context"
    );

    const contextData =
      await contextRes.json();

    setVideoData(
      contextData
    );

    setMessages([
      {
        role: "assistant",
        content: text
      }
    ]);
  }

  async function askQuestion() {

    const userQuestion = question;

    setQuestion("");

    setMessages([
      ...messages,
      {
        role: "user",
        content: userQuestion
      },
      {
        role: "assistant",
        content: ""
      }
    ]);

    const res = await fetch(
      "http://127.0.0.1:8000/stream",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          question: userQuestion
        })
      }
    );

    const reader = res.body?.getReader();

    const decoder = new TextDecoder();

    let answer = "";

    while (true) {

      const { done, value } =
        await reader!.read();

      if (done) break;

      answer += decoder.decode(
        value
      );

      setMessages(prev => {

        const updated = [...prev];

        updated[
          updated.length - 1
        ] = {
          role: "assistant",
          content: answer
        };

        return updated;
      });

    }

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

      {videoData && (

        <div className="grid grid-cols-2 gap-4 mt-8">

          {/* Video A */}

          <div className="border rounded-lg p-5 shadow">

            <h2 className="text-xl font-bold mb-4">
              Video A
            </h2>

            <div className="mb-3">

              <div className="font-semibold">
                {videoData.video_a.title}
              </div>

              <div className="text-sm text-gray-500">
                {videoData.video_a.creator}
              </div>

            </div>

            <div className="grid grid-cols-2 gap-3">

              <div>
                <div className="text-sm">
                  Views
                </div>

                <div className="font-bold">
                  {videoData.video_a.views?.toLocaleString()}
                </div>
              </div>

              <div>
                <div className="text-sm">
                  Likes
                </div>

                <div className="font-bold">
                  {videoData.video_a.likes?.toLocaleString()}
                </div>
              </div>

              <div>
                <div className="text-sm">
                  Comments
                </div>

                <div className="font-bold">
                  {videoData.video_a.comments?.toLocaleString()}
                </div>
              </div>

              <div>
                <div className="text-sm">
                  Engagement
                </div>

                <div className="font-bold">
                  {videoData.video_a.engagement_rate}%
                </div>
              </div>

              <div>
                <div className="text-sm">
                  Duration
                </div>

                <div className="font-bold">
                  {Math.floor(
                    videoData.video_a.duration / 60
                  )}m {videoData.video_a.duration % 60}s
                </div>
              </div>

            </div>

          </div>

          {/* Video B */}

          <div className="border rounded-lg p-5 shadow">

            <h2 className="text-xl font-bold mb-4">
              Video B
            </h2>

            <div className="mb-3">

              <div className="font-semibold">
                {videoData.video_b.title}
              </div>

              <div className="text-sm text-gray-500">
                {videoData.video_b.creator}
              </div>

            </div>

            <div className="grid grid-cols-2 gap-3">

              <div>
                <div className="text-sm">
                  Views
                </div>

                <div className="font-bold">
                  {videoData.video_b.views?.toLocaleString()}
                </div>
              </div>

              <div>
                <div className="text-sm">
                  Likes
                </div>

                <div className="font-bold">
                  {videoData.video_b.likes?.toLocaleString()}
                </div>
              </div>

              <div>
                <div className="text-sm">
                  Comments
                </div>

                <div className="font-bold">
                  {videoData.video_b.comments?.toLocaleString()}
                </div>
              </div>

              <div>
                <div className="text-sm">
                  Engagement
                </div>

                <div className="font-bold">
                  {videoData.video_b.engagement_rate}%
                </div>
              </div>

              <div>
                <div className="text-sm">
                  Duration
                </div>

                <div className="font-bold">
                  {Math.floor(
                    videoData.video_b.duration / 60
                  )}m {videoData.video_b.duration % 60}s
                </div>
              </div>

            </div>

          </div>

        </div>

      )}

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