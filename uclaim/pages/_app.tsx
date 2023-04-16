import { Analytics } from "@vercel/analytics/react";
import type { AppProps } from "next/app";
import "../styles/globals.css";
import { ChakraProvider } from '@chakra-ui/react'
import { SessionProvider } from "next-auth/react";
import React, { useState, useEffect } from "react";

function MyApp({ Component, pageProps: { session, ...pageProps } }: AppProps) {
  return (
    <ChakraProvider>
      <SessionProvider session={session}>
        <Component {...pageProps} />
        <Analytics />
      </SessionProvider>
    </ChakraProvider>
  );
}

export default MyApp;