from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder='client/build', static_url_path='')
CORS(app)
reviews = [
    {
        'photo_url': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'name': 'John Doe',
        'date': '01-01-2023',
        'stars': 5,
        'content': 'I recently purchased this product, and I am absolutely thrilled with its performance. The features are top-notch, and the build quality is exceptional. I highly recommend it to anyone looking for a reliable and powerful solution.',
        'replies': []
    },
    {
        'photo_url': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'name': 'Jane Smith',
        'date': '02-01-2023',
        'stars': 4,
        'content': 'I had a positive experience with the service overall. The customer support was helpful, and the delivery was prompt. However, I believe there could be improvements in certain areas, such as the user interface. Nevertheless, I would consider using the service again.',
        'replies': []
    },
    {
        'photo_url': 'https://plus.unsplash.com/premium_photo-1683121366070-5ceb7e007a97?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'name': 'Alice Johnson',
        'date': '03-01-2023',
        'stars': 3,
        'content': 'The product meets basic requirements but lacks some advanced features I was expecting. The customer service could be more responsive. Overall, it\'s an average experience.',
        'replies': []
    },
    {
        'photo_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'name': 'Bob Williams',
        'date': '04-01-2023',
        'stars': 5,
        'content': 'Outstanding product! It exceeded my expectations in terms of performance and durability. The user interface is intuitive, and the customer support is excellent. Definitely worth the investment.',
        'replies': []
    },
    {
        'photo_url': 'https://plus.unsplash.com/premium_photo-1671656349322-41de944d259b?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'name': 'Eva Davis',
        'date': '05-01-2023',
        'stars': 2,
        'content': 'I encountered several issues with the product, and the customer support was not helpful in resolving them. The overall experience was disappointing, and I wouldn\'t recommend it.',
        'replies': []
    },

{
    'photo_url': 'https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'name': 'Grace Miller',
    'date': '06-01-2023',
    'stars': 4,
    'content': 'After extensive research, I decided to purchase this product, and it has truly exceeded my expectations. The attention to detail in the design is remarkable, and the functionality is superb. I can confidently say that this product has enhanced my daily routine and made tasks much more efficient. Kudos to the developers!',
    'replies': []
},
{
    'photo_url': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHVzZXIlMjBwcm9maWxlfGVufDB8fDB8fHww',
    'name': 'Sam Robinson',
    'date': '07-01-2023',
    'stars': 3,
    'content': 'My experience with this product has been mixed. While certain features are impressive, there are noticeable areas that could be improved for a smoother user experience. I appreciate the effort put into its development, but I hope future updates will address the current limitations.',
    'replies': []
},
{
    'photo_url': 'https://images.unsplash.com/photo-1568602471122-7832951cc4c5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'name': 'Mia Davis',
    'date': '08-01-2023',
    'stars': 5,
    'content': 'I must express my complete satisfaction with this product. From the moment I started using it, I noticed a significant improvement in my daily tasks. The robust features, coupled with a sleek design, make it a standout in its category. I wholeheartedly recommend it to anyone seeking a top-tier solution.',
    'replies': []
},
{
    'photo_url': 'https://plus.unsplash.com/premium_photo-1664298528358-790433ba0815?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'name': 'William Turner',
    'date': '09-01-2023',
    'stars': 2,
    'content': 'Regrettably, my experience with this product has been subpar. The quality falls short of my expectations, and I\'ve encountered several issues that hinder its usability. I believe there\'s significant room for improvement, and I\'m hesitant to recommend it to others based on my current experience.',
    'replies': []
},
{
    'photo_url': 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'name': 'Sophie White',
    'date': '10-01-2023',
    'stars': 4,
    'content': 'I commend the service for its prompt delivery and responsive customer support. These factors significantly contributed to a positive overall experience. While there is always room for enhancement, I am satisfied with the product and appreciate the attention to customer satisfaction demonstrated by the support team.',
    'replies': []
},
]


@app.route('/reviews', methods=['GET', 'POST'])
@cross_origin()
def handle_reviews():
    if request.method == 'GET':
        return jsonify(reviews)
    elif request.method == 'POST':
        data = request.json
        photo_url = data.get('photo_url')
        name = data.get('name')
        date = data.get('date')
        stars = data.get('stars')
        content = data.get('content')

        review = {
            'photo_url': photo_url,
            'name': name,
            'date': date,
            'stars': stars,
            'content': content,
            'replies': []  # to store replies
        }

        reviews.append(review)
        return jsonify({'message': 'Review added successfully'})

@app.route('/reviews/<int:review_id>/reply', methods=['POST'])
@cross_origin()
def add_reply(review_id):
    data = request.json
    reply_content = data.get('reply_content')

    if 0 <= review_id < len(reviews):
        reviews[review_id]['replies'].append(reply_content)
        return jsonify({'message': 'Reply added successfully'})
    else:
        return jsonify({'error': 'Invalid review ID'}), 404

@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
