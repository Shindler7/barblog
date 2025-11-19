const path = require('path');

module.exports = {
    mode: 'production',
    entry: {
        main: './staticshare/frontend/src/main.js',
    },
    output: {
        path: path.resolve(__dirname, 'staticshare/frontend/build'),
        filename: '[name].bundle.js',
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                },
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            },
        ],
    },
};
