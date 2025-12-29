#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main entry point for the Chat Bot application

Usage:
    python main.py

This will start the Flask development server on http://localhost:5000
"""

from chat_bot import app, chatbot
import os

if __name__ == '__main__':
    # Set Flask environment
    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_DEBUG'] = '1'
    
    print("""
    ╔════════════════════════════════════╗
    ║     Welcome to My Chat App!        ║
    ╚════════════════════════════════════╝
    """)
    
    print("Starting the server...")
    print("Open your browser and go to: http://localhost:5000")
    print("Press CTRL+C to stop the server.")
    print()
    
    # Run the Flask app
    app.run(debug=True, host='127.0.0.1', port=5000)
