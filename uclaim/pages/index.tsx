import { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import Footer from "../components/Footer";
import Header from "../components/Header";
import SquigglyLines from "../components/SquigglyLines";
import { Textarea, Button } from '@chakra-ui/react'
import React, { useState, useEffect } from "react";

const Home: NextPage = () => {

  const [prompt, setPrompt] = useState('');
  const [data, setData] = useState('');
  const util = require('util');
  const { exec } = require('child_process');

  // useEffect(() => {
  //   fetch("http://127.0.0.1:5001/data").then((res) =>
  //     res.json().then((data) => {
  //       setData(data)
  //     })
  //   );
  // }, []);

  const handleSubmit = event => {
    event.preventDefault();
    fetch("http://127.0.0.1:5001/data").then((res) =>
      res.json().then((data) => {
        setData(data)
      })
    );
    console.log(data)
  };

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
        <form onSubmit={handleSubmit}>
          <div className="border-t mt-1">
            <Textarea
              placeholder = 'Tell us about yourself!'
              size = 'lg'
              mt = {4}
              padding = {4}
              resize='none'
              h = {200}
              w = {500}
              type='prompt'
              onChange={event => setPrompt(event.currentTarget.value)}
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
              type='submit'
            >
              Button
            </Button>
          </div>
        </form>
        {data &&
          <h2 className="mx-auto max-w-4xl font-display text-3xl font-bold tracking-normal text-gray-300 sm:text-4xl p-6">
            You are{" "}
              <span className="relative whitespace-nowrap text-blue-500">
                <SquigglyLines />
                <span className="relative">{data.data * 100}</span>
              </span>{" "}
            {" "}percent likely to be claimed!
          </h2>
        }
      </main>
      <Footer />
    </div>
  );
};

export default Home;