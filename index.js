// api/index.js
export default function handler(req, res) {
    // Get the User-Agent from the request headers
    const userAgent = req.headers['user-agent'];
  
    // Check if the User-Agent matches the required string
    if (userAgent === 'your-custom-user-agent-string') {
      res.status(200).json({ flag: 'FLAG{your_secret_flag}' });
    } else {
      res.status(403).json({ message: 'Forbidden: Incorrect User-Agent' });
    }
  }
  