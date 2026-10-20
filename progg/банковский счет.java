
class BankAccount {
    //банковский счёт
    protected String owner;
    protected double balance;

    // аккаунт
    public BankAccount(String owner, double balance) {
        this.owner = owner;
        this.balance = balance;
    }

    // пополнение счёта
    public void deposit(double amount) {
        if (amount > 0) {
            balance = balance + amount;
            System.out.println("Счёт пополнен на " + amount + " руб.");
        } else {
            System.out.println("Сумма должна быть больше нуля");
        }
    }

    // снятие денег
    public void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Введите положительную сумму");
        } else if (amount <= balance) {
            balance = balance - amount;
            System.out.println("Снято " + amount + " руб.");
        } else {
            System.out.println("Недостаточно средств");
        }
    }

    // вывод информации о счёте
    public void showInfo() {
        System.out.println("Владелец: " + owner);
        System.out.println("Баланс: " + balance + " руб.");
    }
}
class SavingsAccount extends BankAccount {
    public SavingsAccount(String owner, double balance) { super(owner, balance); }

    @Override
    public void deposit(double amount) {
        if (amount > 0) balance += amount * 1.05;
    }
}



public class Main {
    public static void main(String[] args) {
        // создание банковского счёта
        BankAccount account = new BankAccount("Петя", 5000);
		BankAccount saving = new SavingsAccount("Вася", 5000);

        // выполнение операций для Пети
        account.showInfo();
        account.deposit(2000);
        account.withdraw(1500);

        // вывод информации
        System.out.println("\nПосле операций:");
        account.showInfo();
        
        // выполнение операций для Васи
        System.out.println("\n*********Сберегательный счёт Васи*********");
        saving.showInfo();
        saving.deposit(2000);  
        
        System.out.println("\nПосле операций:");
        saving.showInfo();
    }
}
