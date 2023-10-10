const numberToWords = (num: any) => {
    const ones = [
        '',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ];
    const tens = [
        '',
        '',
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety'
    ];
    const teens = [
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen'
    ];
    const thousands = ['', 'thousand', 'million', 'billion', 'trillion'];

    if (num === 0) {
        return 'zero';
    }

    let words = '';

    for (let i = thousands.length - 1; i >= 0; i--) {
        const divisor = Math.pow(10, 3 * i);

        if (num >= divisor) {
            const quotient = Math.floor(num / divisor);
            num -= quotient * divisor;

            const hundreds = Math.floor(quotient / 100);
            const tensAndOnes = quotient % 100;

            if (hundreds > 0) {
                words += ones[hundreds] + ' hundred ';
            }

            if (tensAndOnes > 0) {
                if (tensAndOnes < 10) {
                    words += ones[tensAndOnes] + ' ';
                } else if (tensAndOnes < 20) {
                    words += teens[tensAndOnes - 10] + ' ';
                } else {
                    const tensDigit = Math.floor(tensAndOnes / 10);
                    const onesDigit = tensAndOnes % 10;

                    words += tens[tensDigit] + ' ';
                    if (onesDigit > 0) {
                        words += ones[onesDigit] + ' ';
                    }
                }
            }

            if (quotient > 0) {
                words += thousands[i] + ' ';
            }
        }
    }

    return words.trim().charAt(0).toUpperCase() + words.slice(1).trim();
};

export default numberToWords;
