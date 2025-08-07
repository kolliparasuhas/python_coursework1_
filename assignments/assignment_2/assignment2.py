def get_messages():
    messages = []
    n = int(input("Enter the number of messages: "))
    for _ in range(n):
        messages.append(input("Enter message (Name: message): "))
    return messages

def count_total_messages(messages):
    print(f"Total messages: {len(messages)}")

def find_unique_users(messages):
    users = set()
    for msg in messages:
        name = msg.split(":")[0]
        users.add(name.strip())
    print("Unique users in the chat:", users)

def count_total_words(messages):
    total_words = sum(len(msg.split(":", 1)[1].split()) for msg in messages if ":" in msg)
    print(f"Total words in the chat: {total_words}")

def average_words_per_message(messages):
    total_words = sum(len(msg.split(":", 1)[1].split()) for msg in messages if ":" in msg)
    average = total_words / len(messages)
    print(f"Average words per message: {average:.2f}")

def longest_message(messages):
    longest = max(messages, key=lambda x: len(x))
    print("Longest message:", longest)

def most_active_user(messages):
    from collections import Counter
    counter = Counter(msg.split(":")[0].strip() for msg in messages if ":" in msg)
    user, count = counter.most_common(1)[0]
    print(f"Most active user: {user} ({count} messages)")

def message_count_by_user(messages):
    user = input("Enter user name: ")
    count = sum(1 for msg in messages if msg.startswith(user + ":"))
    print(f"Messages sent by {user}: {count}")

def most_frequent_word_by_user(messages):
    from collections import Counter
    user = input("Enter user name: ")
    words = []
    for msg in messages:
        if msg.startswith(user + ":"):
            words.extend(msg.split(":", 1)[1].lower().split())
    if words:
        most_common = Counter(words).most_common(1)[0]
        print(f"Most frequent word used by {user}: \"{most_common[0]}\"")
    else:
        print("No messages from this user.")

def first_last_message_by_user(messages):
    user = input("Enter user name: ")
    user_msgs = [msg for msg in messages if msg.startswith(user + ":")]
    if user_msgs:
        print(f"First message by {user}: \"{user_msgs[0]}\"")
        print(f"Last message by {user}: \"{user_msgs[-1]}\"")
    else:
        print(f"No messages found from {user}.")

def check_user_presence(messages):
    user = input("Enter user name to check: ")
    users = set(msg.split(":")[0].strip() for msg in messages if ":" in msg)
    if user in users:
        print(f"User '{user}' is present in the chat.")
    else:
        print(f"User '{user}' not found in the chat.")

def common_repeated_words(messages):
    from collections import Counter
    words = []
    for msg in messages:
        words.extend(msg.split(":", 1)[1].lower().split())
    repeated = {word for word, count in Counter(words).items() if count > 1}
    print("Common repeated words:", repeated)

def user_with_longest_avg_message(messages):
    from collections import defaultdict
    user_words = defaultdict(list)
    for msg in messages:
        if ":" in msg:
            name, content = msg.split(":", 1)
            user_words[name.strip()].append(len(content.strip().split()))
    averages = {user: sum(lengths)/len(lengths) for user, lengths in user_words.items()}
    longest_user = max(averages, key=averages.get)
    print(f"User with longest average message: {longest_user} (avg {averages[longest_user]:.1f} words)")

def count_mentions(messages):
    name = input("Enter name to count mentions: ").lower()
    count = sum(1 for msg in messages if name in msg.split(":", 1)[1].lower())
    print(f"Messages mentioning '{name}': {count}")

def remove_duplicates(messages):
    unique = list(dict.fromkeys(messages))
    print(f"Unique messages count: {len(unique)}")
    for msg in unique:
        print(msg)

def sort_messages(messages):
    for msg in sorted(messages):
        print(msg)

def extract_questions(messages):
    questions = [msg for msg in messages if '?' in msg]
    for q in questions:
        print(q)

def reply_ratio(messages):
    user1 = input("Enter first user: ")
    user2 = input("Enter second user: ")
    replies = 0
    for i in range(1, len(messages)):
        if messages[i-1].startswith(user1 + ":") and messages[i].startswith(user2 + ":"):
            replies += 1
    print(f"Reply ratio from {user2} to {user1}: {replies} replies")

def check_deleted_messages(messages):
    deleted = sum(1 for msg in messages if "This message was deleted" in msg)
    print(f"Deleted messages found: {deleted}")

def menu():
    print("""
Choose an option:
1. Count total number of messages
2. Identify unique users
3. Count total words
4. Calculate average words per message
5. Find the longest message
6. Find the most active user
7. Get message count for a specific user
8. Find most frequently used word by a user
9. Get first and last message by user
10. Check if a user is present
11. Find commonly repeated words
12. Identify user with longest average message
13. Count how many messages mention a user
14. Remove duplicate messages
15. Sort messages alphabetically
16. Extract all questions in chat
17. Calculate reply ratio between two users
18. Check for deleted messages
0. Exit
""")

def main():
    messages = get_messages()
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            count_total_messages(messages)
        elif choice == "2":
            find_unique_users(messages)
        elif choice == "3":
            count_total_words(messages)
        elif choice == "4":
            average_words_per_message(messages)
        elif choice == "5":
            longest_message(messages)
        elif choice == "6":
            most_active_user(messages)
        elif choice == "7":
            message_count_by_user(messages)
        elif choice == "8":
            most_frequent_word_by_user(messages)
        elif choice == "9":
            first_last_message_by_user(messages)
        elif choice == "10":
            check_user_presence(messages)
        elif choice == "11":
            common_repeated_words(messages)
        elif choice == "12":
            user_with_longest_avg_message(messages)
        elif choice == "13":
            count_mentions(messages)
        elif choice == "14":
            remove_duplicates(messages)
        elif choice == "15":
            sort_messages(messages)
        elif choice == "16":
            extract_questions(messages)
        elif choice == "17":
            reply_ratio(messages)
        elif choice == "18":
            check_deleted_messages(messages)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
