const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        trim: true
    },
    email: {
        type: String,
        required: true,
        unique: true,
        lowercase: true,
        trim: true
    },
    password: {
        type: String,
        required: true,
        minlength: 6
    },
    role: {
        type: String,
        enum: ['user', 'admin'], // Define user roles
        default: 'user'
    }
}, { timestamps: true }); // Automatically adds createdAt and updatedAt

const User = mongoose.model('User', userSchema);

module.exports = User;
