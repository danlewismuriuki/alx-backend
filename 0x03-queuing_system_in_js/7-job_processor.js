const kue = require('kue');
const queue = kue.createQueue();
const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    // Track job progress to 0%
    job.progress(0, 100);