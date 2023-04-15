import Document, { Head, Html, Main, NextScript } from "next/document";

class MyDocument extends Document {
  render() {
    let description = "Just Provide a Brief Description of Yourself and We'll Determine if You Are Eligible for Insurance Coverage!";
    let sitename = "UClaim.io";
    let title = "Democratizing Insurance Eligibility With AI";

    return (
      <Html lang="en">
        <Head>
          <link rel="icon" href="/favicon.ico" />
          <meta name="description" content={description} />
          <meta property="og:site_name" content={sitename} />
          <meta property="og:description" content={description} />
          <meta property="og:title" content={title} />
          <meta name="twitter:card" content="summary_large_image" />
          <meta name="twitter:title" content={title} />
          <meta name="twitter:description" content={description} />
        </Head>
        <body className="bg-[#17181C] text-white">
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;