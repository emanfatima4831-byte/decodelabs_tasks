# DecodeLabs AI Internship - Project 3
# AI Recommendation Logic

# Recommendation Data
recommendations = {
    "python": [
        "Python Crash Course",
        "Learn Pandas",
        "Machine Learning Basics"
    ],
    "ai": [
        "AI for Beginners",
        "Neural Networks",
        "ChatGPT Guide"
    ],
    "web": [
        "HTML Course",
        "CSS Course",
        "JavaScript Basics"
    ],
    "cybersecurity": [
        "Ethical Hacking",
        "Network Security",
        "Linux Basics"
    ]
}

# Welcome Message
print("=" * 50)
print("     Welcome to AI Recommendation System")
print("=" * 50)

# Display Available Interests
print("\nAvailable Interests:")
for category in recommendations:
    print("•", category.title())

# Get User Input
interest = input("\nEnter your interest: ").strip().lower()

# Recommendation Logic
if interest in recommendations:
    print("\nRecommended Items for You:\n")

    for i, item in enumerate(recommendations[interest], start=1):
        print(f"{i}. {item}")

else:
    print("\nSorry! No recommendations found.")
    print("Please choose one of the available interests.")

# Thank You Message
print("\nThank you for using the AI Recommendation System!")
print("=" * 50)