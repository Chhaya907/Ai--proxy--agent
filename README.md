 ## AI Work Proxy – Agentic AI Task Automation System
 
 ## Project Overview

AI Work Proxy is an Agentic AI system that autonomously handles tasks when an employee is unavailable.

When the employee status is set to "Away", the AI agent:

Reads the incoming task (simulated email input)

Analyzes and understands the task using Gemini LLM

Creates a structured execution plan

Simulates task execution

Generates a professional reply email

Stores task details in a local SQLite database

This project demonstrates multi-step reasoning, planning, execution, and memory in an autonomous AI workflow.

## Features

Task understanding using Gemini LLM (gemini-2.5-flash)

Automatic execution plan generation

Task execution simulation

Professional email reply generation

Local memory storage using SQLite

Agent activation logic based on employee availability

## System Workflow

Agent checks employee status

If status = "Away", agent activates

Task is analyzed

Execution plan is created

Task is executed

Reply message is generated

Task details are stored in memory

## Tech Stack

Python 3

Google Gemini API

SQLite

smtplib (optional for real email integration)

## Project Structure

main.py – Main workflow controller

task_analyzer.py – Task understanding module

planner.py – Plan generation module

executor.py – Execution and reply generation

memory.py – Database handling

config.py – API configuration

## How to Run

Install dependencies:

```pip install -r requirements.txt```

Add your Gemini API key in config.py:

```GEMINI_API_KEY = "YOUR_API_KEY"```

Run the project:

```python main.py```

## Future Improvements

Real-time email integration (IMAP/SMTP)

Web dashboard interface

Cloud deployment

Multi-agent collaboration system
