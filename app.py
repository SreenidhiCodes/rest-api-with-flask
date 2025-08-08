{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOaBztSuHTXm+t5U0yDnEG2",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SreenidhiCodes/rest-api-with-flask/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install flask-ngrok\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kQjdEg46iEGq",
        "outputId": "28a762bb-b478-4d52-eed6-5f29a43e2e71"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting flask-ngrok\n",
            "  Downloading flask_ngrok-0.0.25-py3-none-any.whl.metadata (1.8 kB)\n",
            "Requirement already satisfied: Flask>=0.8 in /usr/local/lib/python3.11/dist-packages (from flask-ngrok) (3.1.1)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from flask-ngrok) (2.32.3)\n",
            "Requirement already satisfied: blinker>=1.9.0 in /usr/local/lib/python3.11/dist-packages (from Flask>=0.8->flask-ngrok) (1.9.0)\n",
            "Requirement already satisfied: click>=8.1.3 in /usr/local/lib/python3.11/dist-packages (from Flask>=0.8->flask-ngrok) (8.2.1)\n",
            "Requirement already satisfied: itsdangerous>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from Flask>=0.8->flask-ngrok) (2.2.0)\n",
            "Requirement already satisfied: jinja2>=3.1.2 in /usr/local/lib/python3.11/dist-packages (from Flask>=0.8->flask-ngrok) (3.1.6)\n",
            "Requirement already satisfied: markupsafe>=2.1.1 in /usr/local/lib/python3.11/dist-packages (from Flask>=0.8->flask-ngrok) (3.0.2)\n",
            "Requirement already satisfied: werkzeug>=3.1.0 in /usr/local/lib/python3.11/dist-packages (from Flask>=0.8->flask-ngrok) (3.1.3)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->flask-ngrok) (3.4.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->flask-ngrok) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->flask-ngrok) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->flask-ngrok) (2025.8.3)\n",
            "Downloading flask_ngrok-0.0.25-py3-none-any.whl (3.1 kB)\n",
            "Installing collected packages: flask-ngrok\n",
            "Successfully installed flask-ngrok-0.0.25\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from flask import Flask, request, jsonify\n",
        "\n",
        "app = Flask(__name__)\n",
        "\n",
        "# In-memory user data store\n",
        "users = {}\n",
        "\n",
        "# GET: Retrieve all users\n",
        "@app.route('/users', methods=['GET'])\n",
        "def get_users():\n",
        "    return jsonify(users), 200\n",
        "\n",
        "# GET: Retrieve a single user by ID\n",
        "@app.route('/users/<user_id>', methods=['GET'])\n",
        "def get_user(user_id):\n",
        "    user = users.get(user_id)\n",
        "    if user:\n",
        "        return jsonify({user_id: user}), 200\n",
        "    return jsonify({'error': 'User not found'}), 404\n",
        "\n",
        "# POST: Add a new user\n",
        "@app.route('/users', methods=['POST'])\n",
        "def create_user():\n",
        "    data = request.get_json()\n",
        "    user_id = data.get('id')\n",
        "    name = data.get('name')\n",
        "\n",
        "    if not user_id or not name:\n",
        "        return jsonify({'error': 'Both id and name are required'}), 400\n",
        "\n",
        "    if user_id in users:\n",
        "        return jsonify({'error': 'User already exists'}), 409\n",
        "\n",
        "    users[user_id] = name\n",
        "    return jsonify({'message': 'User added successfully'}), 201\n",
        "\n",
        "# PUT: Update an existing user\n",
        "@app.route('/users/<user_id>', methods=['PUT'])\n",
        "def update_user(user_id):\n",
        "    if user_id not in users:\n",
        "        return jsonify({'error': 'User not found'}), 404\n",
        "\n",
        "    data = request.get_json()\n",
        "    name = data.get('name')\n",
        "\n",
        "    if not name:\n",
        "        return jsonify({'error': 'Name is required'}), 400\n",
        "\n",
        "    users[user_id] = name\n",
        "    return jsonify({'message': 'User updated successfully'}), 200\n",
        "\n",
        "# DELETE: Delete a user\n",
        "@app.route('/users/<user_id>', methods=['DELETE'])\n",
        "def delete_user(user_id):\n",
        "    if user_id not in users:\n",
        "        return jsonify({'error': 'User not found'}), 404\n",
        "\n",
        "    del users[user_id]\n",
        "    return jsonify({'message': 'User deleted successfully'}), 200\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    app.run(debug=True)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uJvtlYSdEqR6",
        "outputId": "3b3b9731-1d43-4e99-d85f-93932b4cf3d6"
      },
      "execution_count": 1,
      "outputs": [
        {
          "metadata": {
            "tags": null
          },
          "name": "stdout",
          "output_type": "stream",
          "text": [
            " * Serving Flask app '__main__'\n",
            " * Debug mode: on\n"
          ]
        },
        {
          "metadata": {
            "tags": null
          },
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "INFO:werkzeug:\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n",
            " * Running on http://127.0.0.1:5000\n",
            "INFO:werkzeug:\u001b[33mPress CTRL+C to quit\u001b[0m\n",
            "INFO:werkzeug: * Restarting with stat\n"
          ]
        }
      ]
    }
  ]
}