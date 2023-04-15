import { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Footer from "../components/Footer";
import Header from "../components/Header";
import SquigglyLines from "../components/SquigglyLines";
import { Textarea, Button } from '@chakra-ui/react'

const Home: NextPage = () => {
  return (
    <div className="flex max-w-6xl mx-auto flex-col items-center justify-center py-2 min-h-screen">
      <Head>
        <title>UClaim</title>
      </Head>
      <main className="flex flex-1 w-full flex-col items-center justify-center text-center px-4 sm:mt-20 mt-20 background-gradient">
        <h1 className="mx-auto max-w-4xl font-display text-5xl font-bold tracking-normal text-gray-300 sm:text-7xl">
          Democratizing Insurance Eligibility {" "}
          <span className="relative whitespace-nowrap text-blue-500">
            <SquigglyLines />
            <span className="relative">With AI</span>
          </span>{" "}
        </h1>
        <h2 className="mx-auto mt-12 max-w-xl text-lg sm:text-gray-400 text-gray-500 leading-7">
          Just Provide a Brief Description of Yourself and We'll Determine if You Are Eligible for Insurance Coverage!
        </h2>
        <div>
          <div className="border-t mt-1">
            <Textarea
              placeholder = 'Tell us about yourself!'
              size = 'lg'
              mt = {4}
              padding = {4}
              resize='none'
              h = {200}
              w = {500}
            />
          </div>
          <div className = "py-4 text-right">
            <Button
              colorScheme='blue'
              variant='solid'
              color='white'
              fontSize={18}
              size='md'
              height='48px'
              width='200px'
              border='2px'
              borderColor='white'
            >
              Button
            </Button>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default Home;