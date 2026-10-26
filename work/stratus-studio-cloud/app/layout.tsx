import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Stratus Studio",
  description: "Private Stratus document editor and coding workspace.",
  icons: {
    icon: "/favicon.svg?v=studio-white-1",
    shortcut: "/favicon.svg?v=studio-white-1",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
