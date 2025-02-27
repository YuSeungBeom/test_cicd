# Generated by Django 5.1.5 on 2025-01-22 06:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='도서명')),
                ('author', models.CharField(max_length=100, verbose_name='저자')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('publisher', models.CharField(max_length=100, verbose_name='출판사')),
                ('total_quantity', models.PositiveIntegerField(default=1, verbose_name='전체 수량')),
                ('available_quantity', models.PositiveIntegerField(default=1, verbose_name='대출 가능 수량')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
            ],
            options={
                'verbose_name': '도서',
                'verbose_name_plural': '도서 목록',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ACTIVE', '대출중'), ('OVERDUE', '연체'), ('RETURNED', '반납완료')], default='ACTIVE', max_length=10, verbose_name='상태')),
                ('loan_date', models.DateTimeField(auto_now_add=True, verbose_name='대출일')),
                ('due_date', models.DateTimeField(verbose_name='반납예정일')),
                ('returned_date', models.DateTimeField(blank=True, null=True, verbose_name='반납일')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='도서')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '대출',
                'verbose_name_plural': '대출 목록',
                'ordering': ['-loan_date'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WAITING', '대기중'), ('AVAILABLE', '대출가능'), ('CANCELLED', '취소됨')], default='WAITING', max_length=10, verbose_name='상태')),
                ('reserved_date', models.DateTimeField(auto_now_add=True, verbose_name='예약일')),
                ('expiry_date', models.DateTimeField(verbose_name='예약만료일')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='도서')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '예약',
                'verbose_name_plural': '예약 목록',
                'ordering': ['reserved_date'],
                'unique_together': {('user', 'book', 'status')},
            },
        ),
    ]
