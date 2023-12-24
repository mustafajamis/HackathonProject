# Perl to Python Code Converter using OpenAI's ChatGPT

Ever wished converting Perl code to Python could be a breeze? Well, here's a nifty script that does just that! Powered by OpenAI's ChatGPT, this project takes your Perl code, tosses it to the GPT-3 model, gets back shiny Python code, and even tries running it for you.

# How It Rolls:

Seamless Conversion: No more manual translation. Let ChatGPT do the heavy lifting for you.
Execution Handling: The script gives the Python code a whirl and deals with any hiccups along the way.
Error Correction Exploration: We're toying with the idea of using error messages to improve the process. It's a work in progress!
Under the Hood:

This script chats with the OpenAI API, throws in your Perl code, and catches the Python magic. We've stress-tested it with various Perl files to make sure it's up to the task.

# Results and Roadblocks:

So far, so good! It tackles straightforward Perl-to-Python conversions like a champ. But, we're working on smoothing out the bumps, especially when things get a bit complex.

# Challenges Faced:

Comprehensive Error Handling: Covering all bases, from reading Perl to chatting with ChatGPT.
ChatGPT Feedback Loop: Figuring out how to use error messages to make ChatGPT even smarter.
Flexibility Boost: Let's make those file paths more flexible, shall we?
Model Validation: Making sure we're using the right engine for the job.
Sharper Code Extraction: Enhancing how we grab that Python gold from ChatGPT's response.
