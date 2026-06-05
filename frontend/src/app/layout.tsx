import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Creator's Intelligent Assistant",
  description:
    "Compare Creator's videos, analyze engagement, and ask AI-powered follow-up questions in a mobile-first Assistant interface.",
  keywords: [
    "Creator's Intelligent",
    "video comparison",
    "Assistant",
    "engagement analysis",
    "YouTube insights",
    "AI assistant",
  ],
  openGraph: {
    title: "Creator's Intelligent Assistant",
    description:
      "Compare Creator's videos, discover engagement winners, and ask follow-up questions with an AI-powered Assistant tool.",
    type: "website",
  },
  twitter: {
    card: "summary",
    title: "Creator's Intelligent Assistant",
    description:
      "Compare Creator's videos with AI-driven insights and engagement analysis.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
