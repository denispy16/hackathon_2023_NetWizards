# Generated by Django 4.2 on 2023-04-22 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_where', models.CharField(max_length=50, verbose_name='от куда')),
                ('to_where', models.CharField(max_length=50, verbose_name='куда')),
                ('status', models.BooleanField(default=True, verbose_name='Статус отправки')),
                ('how_many', models.CharField(max_length=50, verbose_name='Колличество')),
                ('buyer', models.CharField(max_length=255, verbose_name='Покупатель')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Статус оплаты')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('description', models.CharField(blank=True, verbose_name='Описание')),
                ('photo', models.CharField(blank=True, max_length=300, verbose_name='Фото')),
                ('available', models.BooleanField(default=True, verbose_name='Наличие')),
                ('on_stock', models.CharField(max_length=255, verbose_name='Доступное количество')),
                ('price', models.CharField(max_length=10, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wb_app.category', verbose_name='Категории')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wb_app.transaction', verbose_name='транзакция')),
            ],
        ),
    ]
