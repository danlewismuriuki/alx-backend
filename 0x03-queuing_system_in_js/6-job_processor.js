const kue = require('kue');

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${PHONE_NUMBER}, with message: ${MESSAGE}`);
};

queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = jb.data;
    sendNotification(phoneNumber, message);
    done();
});